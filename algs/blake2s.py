import config

class Blake2s:
    def __init__(self):
        self.args = [
            "./vendors/ccminer/ccminer", 
            "-a", "blake2s", 
            "-o", "stratum+tcp://blake2s.eu.nicehash.com:3361", 
            "-u", "%s.%s" % (config.btc_address, config.rig_name)
        ]
