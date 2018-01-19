import requests
from units import *
# import algorithms

def getCurrentStats():
    #TODO: use https://api.nicehash.com/api?method=simplemultialgo.info instead?
    r = requests.get("https://api.nicehash.com/api?method=simplemultialgo.info")
    stats = r.json()["result"]["simplemultialgo"]

    res = []
    for alg in stats:
        algId = alg["algo"]
        # units = algorithms.getUnits(algId)
        res.append([algId, float(alg["paying"])])

        # if algId == 7:
        #     print(units)
        #     print(float(alg["price"]))
        #     print(units(float(alg["price"])))

    return res
