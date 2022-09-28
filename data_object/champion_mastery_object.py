from data_object.tojson_object import ToJsonObject


class ChampionMasteryObject(ToJsonObject):
    championId: int
    championPoints: int

    def __init__(self):
        self.championId = 0
        self.championPoints = 0
