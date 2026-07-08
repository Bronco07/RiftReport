from project import parse_riot_id, calculate_winrate, calculate_average_kda, get_kda

def test_parse_riot_id():
    assert parse_riot_id("Bronco#PDD") == ("Bronco", "PDD")
    assert parse_riot_id("Faker#best") == ("Faker", "best")
    assert parse_riot_id("LeaguePlayer#123") == ("LeaguePlayer", "123")

def test_calculate_winrate():
    test = [
    {"win": True},
    {"win": False},
    {"win": True},
    {"win": False},
    ]
    assert calculate_winrate(test) == 50

def test_get_kda():
    match = {"kills": 10, "assists": 10, "deaths": 2}
    assert get_kda(match) == 10
    match = {"kills": 2, "assists": 4, "deaths": 0}
    assert get_kda(match) == 6
