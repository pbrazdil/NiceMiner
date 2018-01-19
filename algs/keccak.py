import config

class Keccak:
    def __init__(self):
        self.args = [
            "./vendors/ccminer/ccminer", 
            "-a", "keccak", 
            "-o", "stratum+tcp://keccak.eu.nicehash.com:3348", 
            "-u", "%s.%s" % (config.btc_address, config.rig_name)
        ]
