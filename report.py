def display_report(nickname, server, rank, most_played_champs, winrate, avg_kda, best_champ):
    report = f"Player: {nickname}\n"
    report += f"Server: {server}\n"
    report += f"Rank: {rank}\n"
    report += ("_" * 30 + "\n\n")

    for index, (champ, points) in enumerate(most_played_champs.items()):
        report += f"{index + 1}. {champ}: {points} mastery points\n"

    report += ("_" * 30 + "\n\n")
    report += f"Winrate: {winrate} %\n"
    report += f"Average KDA: {round(avg_kda, 2)}\n"
    report += f"Best champion: {best_champ}"

    return report