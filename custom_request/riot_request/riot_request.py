from data_object.riot_request_object import RiotRequestObject
from config.manage_key import get_key

routing = {
    "BR1": "br1.api.riotgames.com",
    "EUN1": "eun1.api.riotgames.com",
    "EUW1": "euw1.api.riotgames.com",
    "JP1": "jp1.api.riotgames.com",
    "KR": "kr.api.riotgames.com",
    "LA1": "la1.api.riotgames.com",
    "LA2": "la2.api.riotgames.com",
    "NA1": "na1.api.riotgames.com",
    "OC1": "oc1.api.riotgames.com",
    "TR1": "tr1.api.riotgames.com",
    "RU": "ru.api.riotgames.com",
    "AMERICAS": "americas.api.riotgames.com",
    "ASIA": "asia.api.riotgames.com",
    "EUROPE": "europe.api.riotgames.com",
    "SEA": "sea.api.riotgames.com",
}

http_prefix = "https://"


def build_request(region: str) -> RiotRequestObject:
    region_path = routing[region]
    api_key = get_key('RIOT_API_KEY')

    riot_request_object = RiotRequestObject()
    riot_request_object.url = http_prefix + region_path
    riot_request_object.headers = {"X-Riot-Token": api_key}

    return riot_request_object

