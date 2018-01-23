import nicehash.algorithms
from utils.units import *
import logging

class NiceHashGTX1080Ti: 
    def __init__(self):
        logger = logging.getLogger()
        self.stats = {}

        self.addStat("Nist5", MHs(71.62))
        self.addStat("Keccak", MHs(1275.0))
        self.addStat("NeoScrypt", MHs(0.37))
        self.addStat("Lyra2REv2", MHs(60.0))
        self.addStat("DaggerHashimoto", MHs(35.0))
        self.addStat("Decred", GHs(4.6))
        self.addStat("CryptoNight", kHs(0.76))
        self.addStat("Lbry", GHs(0.47))
        self.addStat("Equihash", Sols(630))
        self.addStat("Pascal", GHs(1.76))
        self.addStat("X11Gost", MHs(16.2))
        self.addStat("Sia", GHs(2.96))
        self.addStat("Blake2s", GHs(6.98))

    def addStat(self, algname, speed):
        algId = nicehash.algorithms.nameToAlgoId(algname)
        self.stats[algId] = speed