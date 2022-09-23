from flask_restful import Resource
from custom_request.riot_request import summoner_request


class Summoner(Resource):
    summoner_data: summoner_request.SummonerObject

    def get(self, username):
        self.summoner_data = summoner_request.get_data("EUW1", username)
        return self.summoner_data.toJSON()
