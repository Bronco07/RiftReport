def extract_player_stats(matches, puuid):
    results = []
    for match in matches:
        for player in match["info"]["participants"]:
            if player["puuid"] == puuid:
                results.append(player)
    return results


def calculate_winrate(matches):
    wins = sum(match["win"] for match in matches)
    return (wins / len(matches)) * 100


def calculate_average_kda(matches):
    kdas = [get_kda(match) for match in matches]
    return sum(kdas) / len(kdas)


def get_kda(match):
    try:
        return (match["kills"] + match["assists"]) / match["deaths"]
    except ZeroDivisionError:
        return match["kills"] + match["assists"]


def find_best_kda_champion(matches):
    best_match = max(matches, key=get_kda)
    return best_match["championName"]