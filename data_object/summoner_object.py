from data_object.champion_mastery_object import ChampionMasteryObject
from data_object.tojson_object import ToJsonObject


class SummonerObject(ToJsonObject):
    name: str
    puuid: str
    summonerLevel: int
    profileIconId: int
    championMasteryList: list[ChampionMasteryObject]
    rankInformation: list[RankInformationObject]

    def __init__(self):
        self.name = ''
        self.puuid = ''
        self.summonerLevel = 0
        self.profileIconId = 0
