from data_object.tojson_object import ToJsonObject


class RankInformationObject(ToJsonObject):
    queueType: str
    tier: str
    rank: str
    wins: int
    losses: int
    leaguePoints: int

    def __init__(self):
        self.queueType = ''
        self.tier = ''
        self.rank = ''
        self.wins = 0
        self.losses = 0
        self.leaguePoints = 0
