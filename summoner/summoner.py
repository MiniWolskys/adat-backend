from flask_restful import Resource
from custom_request.riot_request import summoner_request


class Summoner(Resource):
    summoner_data: summoner_request.SummonerObject

    def get(self, username):
        self.summoner_data = summoner_request.get_data(username)
        return self.summoner_data.toJSON()

    def get_summoner_data(self) -> summoner_request.SummonerObject:
        return self.summoner_data

    def get_summoner_name(self) -> str:
        return self.summoner_data.name

    def get_summoner_puuid(self) -> str:
        return self.summoner_data.puuid

    def get_summoner_level(self) -> int:
        return self.summoner_data.summonerLevel

    def get_summoner_icon(self) -> int:
        return self.summoner_data.profileIconId
