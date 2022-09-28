from data_object.summoner_object import SummonerObject
from custom_request.riot_request import riot_request
from data_object.factory.custom_object_factory import generate_object_from_riot_api
import requests

url_summoner_by_name = '/lol/summoner/v4/summoners/by-name/'


def get_data(region: str, username: str) -> SummonerObject:
    request = riot_request.build_request(region)
    request.url += url_summoner_by_name + username
    ## TODO: Implement custom requesting tool for Riot API
    res = requests.get(request.url, headers=request.headers)
    if res.status_code != 200:
        # ERROR MANAGEMENT
        pass
    return generate_object_from_riot_api(res, SummonerObject)
