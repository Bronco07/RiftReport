from api import parse_riot_id
from analysis import calculate_winrate, get_kda


def test_parse_riot_id():
    assert parse_riot_id("Bronco#PDD") == ("Bronco", "PDD")
    assert parse_riot_id("Faker#best") == ("Faker", "best")
    assert parse_riot_id("LeaguePlayer#123") == ("LeaguePlayer", "123")


def test_calculate_winrate():
    matches = [
        {"win": True},
        {"win": False},
        {"win": True},
        {"win": False},
    ]

    assert calculate_winrate(matches) == 50


def test_get_kda():
    match = {"kills": 10, "assists": 10, "deaths": 2}
    assert get_kda(match) == 10

    match = {"kills": 2, "assists": 4, "deaths": 0}
    assert get_kda(match) == 6