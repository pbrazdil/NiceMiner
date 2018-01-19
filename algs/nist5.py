import config

class Nist5:
    def __init__(self):
        self.args = [
            "./vendors/ccminer/ccminer", 
            "-i", "26", 
            "-a", "nist5", 
            "-o", "stratum+tcp://nist5.eu.nicehash.com:3340", 
            "-u", "%s.%s" % (config.btc_address, config.rig_name)
        ]
