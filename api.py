import requests
import sys


def parse_riot_id(riot_id):
    game_name, tag_line = riot_id.split("#")
    return game_name, tag_line


def fetch_account(game_name, tag_line, api_key):
    url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        sys.exit("Unable to find player")
    return response.json()


def fetch_rank(puuid, server, api_key):
    url = f"https://{server}.api.riotgames.com/lol/league/v4/entries/by-puuid/{puuid}?api_key={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit("Incorrect player data")

    ranked = response.json()
    for rank in ranked:
        if rank["queueType"] == "RANKED_SOLO_5x5":
            return f'{rank["tier"]} {rank["rank"]}'

    return "Unranked"


def fetch_masteries(puuid, server, api_key):
    url = f"https://{server}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top?count=3&api_key={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit("Unable to find champion masteries")

    masteries = response.json()
    sorted_masteries = sorted(masteries, key=lambda x: x["championPoints"], reverse=True)

    top_champions = {}
    for champ in sorted_masteries:
        top_champions[champ["championId"]] = champ["championPoints"]

    return top_champions


def fetch_champion_data():
    version_response = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")
    versions = version_response.json()
    latest_version = versions[0]

    champ_response = requests.get(
        f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/champion.json"
    )
    champ_data = champ_response.json()

    id_to_name = {}
    for champ_name, info in champ_data["data"].items():
        id_to_name[int(info["key"])] = champ_name

    return id_to_name


def combine_masteries_with_names(masteries, id_to_name):
    named_masteries = {}
    for champ_id, points in masteries.items():
        champ_name = id_to_name[champ_id]
        named_masteries[champ_name] = points
    return named_masteries


def server_to_region(server):
    if server in ["na1", "br1", "la1", "la2", "oc1"]:
        return "americas"
    if server in ["euw1", "eun1", "tr1", "ru1"]:
        return "europe"
    if server in ["kr", "jp1"]:
        return "asia"
    if server in ["sg2", "tw2", "vn2"]:
        return "sea"

    sys.exit("Incorrect server")


def fetch_match_ids(puuid, server, api_key):
    region = server_to_region(server)
    url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=10&api_key={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        sys.exit("Unable to find player's matches")
    return response.json()


def fetch_match_details(match_ids, server, api_key):
    results = []
    region = server_to_region(server)

    for match in match_ids:
        url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match}?api_key={api_key}"
        response = requests.get(url)
        if response.status_code != 200:
            sys.exit("Unable to find player's matches")
        results.append(response.json())

    return results