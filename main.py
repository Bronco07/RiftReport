import os

from dotenv import load_dotenv

from api import (
    parse_riot_id,
    fetch_account,
    fetch_rank,
    fetch_masteries,
    fetch_champion_data,
    combine_masteries_with_names,
    fetch_match_ids,
    fetch_match_details,
)
from analysis import (
    extract_player_stats,
    calculate_average_kda,
    calculate_winrate,
    find_best_kda_champion,
)
from report import display_report


load_dotenv()

API_KEY = os.getenv("RIOT_API_KEY")


def main():
    nickname = input("Enter Riot ID (GameName#TAG): ").strip()
    server = input("Enter server (e.g. eun1): ").strip()

    name, tag = parse_riot_id(nickname)
    account = fetch_account(name, tag, API_KEY)

    rank = fetch_rank(account["puuid"], server, API_KEY)
    masteries = fetch_masteries(account["puuid"], server, API_KEY)
    id_to_name = fetch_champion_data()
    named_masteries = combine_masteries_with_names(masteries, id_to_name)

    match_ids = fetch_match_ids(account["puuid"], server, API_KEY)
    matches = fetch_match_details(match_ids, server, API_KEY)
    player_stats = extract_player_stats(matches, account["puuid"])

    winrate = calculate_winrate(player_stats)
    avg_kda = calculate_average_kda(player_stats)
    best_champ = find_best_kda_champion(player_stats)

    print(
        display_report(
            nickname,
            server,
            rank,
            named_masteries,
            winrate,
            avg_kda,
            best_champ,
        )
    )


if __name__ == "__main__":
    main()