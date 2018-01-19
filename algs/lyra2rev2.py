import config

class Lyra2REv2:
    def __init__(self):
        self.args = [
            "./vendors/ccminer/ccminer", 
            "-a", "lyra2v2", 
            "-o", "stratum+tcp://lyra2rev2.eu.nicehash.com:3347", 
            "-u", "%s.%s" % (config.btc_address, config.rig_name)
        ]
