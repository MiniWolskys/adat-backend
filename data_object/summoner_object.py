from data_object.tojson_object import ToJsonObject


class SummonerObject(ToJsonObject):
    name: str
    puuid: str
    summonerLevel: int
    profileIconId: int

    def __init__(self):
        self.name = ''
        self.puuid = ''
        self.summonerLevel = 0
        self.profileIconId = 0
