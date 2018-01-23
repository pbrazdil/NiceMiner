import logging

import nvidia.devices as devices

def printGPUs():
    logger = logging.getLogger()
    
    logger.info("Driver Version: %s" % devices.get_driver_version())

    for i, d in enumerate(devices.get()):
        logger.info("Device %d: %s, %.2fW" % (i, d[1], d[2]))