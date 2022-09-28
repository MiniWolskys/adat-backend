from requests import Response


def generate_object_from_riot_api(data: any, target: any):
    ret = target()
    for attr, val in ret.__dict__.items():
        if attr in data:
            setattr(ret, attr, data[attr])
    return ret
