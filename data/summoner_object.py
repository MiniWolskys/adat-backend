from data.tojson_object import ToJsonObject


class SummonerObject(ToJsonObject):
    name: str
    puuid: str
    summonerLevel: int
    profileIconId: int

    def __init__(self, name: str, puuid: str, summonerLevel: int, profileIconId: int):
        self.name = name
        self.puuid = puuid
        self.summonerLevel = summonerLevel
        self. profileIconId = profileIconId
