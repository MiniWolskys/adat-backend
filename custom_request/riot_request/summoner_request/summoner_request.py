from data_object.summoner_object import SummonerObject
from custom_request.riot_request import riot_request
from data_object.factory.custom_object_factory import generate_object_from_riot_api
from requests import Response
import requests

url_summoner_by_name = '/lol/summoner/v4/summoners/by-name/'


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
    summoner_data = generate_object_from_riot_api(res, SummonerObject)
    return summoner_data
