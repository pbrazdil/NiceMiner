import config

class Blake2s:
    def getParams(self):
        return [
            "./vendors/ccminer-tpruvot/run", 
            "-a", "blake2s", 
            "-i", "30",
            "-o", "stratum+tcp://blake2s.%s.nicehash.com:3361" % config.nicehash_location, 
            "-u", "%s.%s" % (config.btc_address, config.rig_name)
        ]
