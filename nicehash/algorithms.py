from utils.units import *


algorithms = ["Scrypt", "SHA256", "ScryptNf", "X11", "X13", "Keccak", "X15", "Nist5", "NeoScrypt", "Lyra2RE", "WhirlpoolX", "Qubit", "Quark", "Axiom", "Lyra2REv2", "ScryptJaneNf16", "Blake256r8", "Blake256r14", "Blake256r8vnl", "Hodl", "DaggerHashimoto", "Decred", "CryptoNight", "Lbry", "Equihash", "Pascal", "X11Gost", "Sia", "Blake2s", "Skunk"] 

def algoIdToName(id):
    return algorithms[id]

def nameToAlgoId(name):
    return algorithms.index(name)

