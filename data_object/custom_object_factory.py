from requests import Response


def generate_object_from_riot_api(res: Response, target: any):
    ret = target()
    data = res.json()
    for attr, val in ret.__dict__.items():
        setattr(ret, attr, data[attr])
    return ret
