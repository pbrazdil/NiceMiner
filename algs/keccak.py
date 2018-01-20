import config

class Keccak:
    def getParams(self):
        return [
            "./vendors/ccminer-klaust/run", 
            "-a", "keccak", 
            "-i", "30",
            "-o", "stratum+tcp://keccak.%s.nicehash.com:3338" % config.nicehash_location, 
            "-u", "%s.%s" % (config.btc_address, config.rig_name)
        ]
