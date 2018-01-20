import config

class Lyra2REv2:
    def getParams(self):
        return [
            "./vendors/ccminer-klaust/run", 
            "-a", "lyra2v2", 
            "--no-cpu-verify",
            "--cpu-priority", "5",
            "-o", "stratum+tcp://lyra2rev2.%s.nicehash.com:3347" % config.nicehash_location, 
            "-u", "%s.%s" % (config.btc_address, config.rig_name)
        ]
