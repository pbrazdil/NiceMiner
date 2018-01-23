import time
import os
import sys
import logging

import config
import nicehash.api
from gpus.gtx1080ti import GTX1080Ti
import nvidia.devices
import stats.nvidia
from stats.profitability import ProfitabilityStats
from utils.units import *
import utils.shell as shell
from miner_manager import MinerManager
import papertrail

def delimiter():
    logger = logging.getLogger()
    logger.info("=" * 100)

def check():
    nicehashstats = nicehash.api.getCurrentStats()

    s = ProfitabilityStats(gpuType, gpuCount)
    s.print(nicehashstats, limit=6)

    return s.calculate(nicehashstats)

logger = papertrail.setup()
if __name__ == "__main__":
    activeAlgorithm = None

    gpuType = GTX1080Ti()
    gpuCount = nvidia.devices.count()
    
    manager = MinerManager()
    
    logger.info("Starting niceminer...")
    logger.info("Supported algs: %s" % str(manager.supported()))
    logger.info("Found %d GPUs" % gpuCount)
    stats.nvidia.printGPUs()

    while True:
        delimiter()
        stats = check()
        manager.update(stats)
        delimiter()
        if manager.alg_switched:
            time.sleep(config.minimum_time_for_running_alg)

        time.sleep(config.check_profitability_interval)
    
