import logging
import socket
from logging.handlers import SysLogHandler

import config

def setup():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    syslog = SysLogHandler(address=(config.papertrail_url, config.papertrail_port))
    formatter = logging.Formatter(config.rig_name + ': %(message)s')

    syslog.setFormatter(formatter)
    logger.addHandler(syslog)

    return logger

