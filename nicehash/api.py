import requests
from utils.units import *
import logging

def getCurrentStats():
    logging.getLogger("requests").setLevel(logging.WARNING)
    r = requests.get("https://api.nicehash.com/api?method=simplemultialgo.info")
    stats = r.json()["result"]["simplemultialgo"]

    res = []
    for alg in stats:
        algId = alg["algo"]
        res.append([algId, float(alg["paying"])])

    return res
