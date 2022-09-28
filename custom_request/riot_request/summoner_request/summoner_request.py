from data_object.champion_mastery_object import ChampionMasteryObject
from data_object.rank_information_object import RankInformationObject
from data_object.summoner_object import SummonerObject
from custom_request.riot_request import riot_request
from data_object.factory.custom_object_factory import generate_object_from_riot_api
from requests import Response
import requests

url_summoner_by_name = '/lol/summoner/v4/summoners/by-name/'
url_mastery_by_id = '/lol/champion-mastery/v4/champion-masteries/by-summoner/'
url_league_by_id = '/lol/league/v4/entries/by-summoner/'


def get_rank_data(region: str, summoner_id: str) -> list[RankInformationObject]:
    request = riot_request.build_request(region)
    request.url += url_league_by_id + summoner_id
    res = requests.get(request.url, headers=request.headers)
    rank_list: list[RankInformationObject] = []
    for rank_data in res.json():
        rank_list.append(generate_object_from_riot_api(rank_data, RankInformationObject))
    return rank_list


def get_top_mastery_data(region: str, summoner_id: str, count: int) -> list[ChampionMasteryObject]:
    request = riot_request.build_request(region)
    request.url += url_mastery_by_id + summoner_id + '/top?count=' + str(count)
    res = requests.get(request.url, headers=request.headers)
    mastery_list: list[ChampionMasteryObject] = []
    for mastery_data in res.json():
        mastery_list.append(generate_object_from_riot_api(mastery_data, ChampionMasteryObject))
    return mastery_list


def get_summoner_data(region: str, username: str) -> Response:
    request = riot_request.build_request(region)
    request.url += url_summoner_by_name + username
    ## TODO: Implement custom requesting tool for Riot API
    return requests.get(request.url, headers=request.headers)


def get_data(region: str, username: str) -> SummonerObject:
    res = get_summoner_data(region, username)
    if res.status_code != 200:
        # ERROR MANAGEMENT
        pass
    summoner_data: SummonerObject = generate_object_from_riot_api(res.json(), SummonerObject)
    summoner_data.championMasteryList = get_top_mastery_data(region, summoner_data.id, 5)
    summoner_data.rankInformation = get_rank_data(region, summoner_data.id)
    return summoner_data
