import tempfile
import json

import config
import nvidia.devices

class Equihash:
    def getParams(self):
        input_json = [
	        {"time":1,"commands":[
		        {"id":1,"method":"algorithm.add","params":[
                    "equihash",
                    "equihash.%s.nicehash.com:3357" % config.nicehash_location,
                    "%s.%s" % (config.btc_address, config.rig_name)
                ]}
	        ]},
	        {"time":2,"commands":[
                {"id":1,"method":"worker.add","params":["0",str(i)]} for i in range(0, nvidia.devices.count())
        	]},
            # {"time":10,"commands":[
		    #     {"id":1,"method":"worker.reset","params":[str(i)]} for i in range(0, nvidia.devices.numberOfGPUs())
		    # ]},
            {"time":10,"loop":15,"commands":[
	  	        {"id":1,"method":"algorithm.print.speeds","params":[]}
	        ]},
        ]

        input_file = tempfile.NamedTemporaryFile(delete=False)  
        # input_file.write(json.dumps(input_json))
        with open(input_file.name, 'w') as file:
            file.write(json.dumps(input_json))

        return [
            "./vendors/excavator/excavator", 
            # "-c", "./vendors/excavator/scripts/equihash.json"
            "-c", input_file.name
        ]


        
