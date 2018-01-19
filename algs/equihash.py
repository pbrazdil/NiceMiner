import config

class Equihash:
    def __init__(self):
        self.args = [
            "./vendors/ccminer/ccminer", 
            "-a", "equihash", 
            "-o", "stratum+tcp://equihash.eu.nicehash.com:3357", 
            "-u", "%s.%s" % (config.btc_address, config.rig_name)
        ]
