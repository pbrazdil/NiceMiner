import time
import os
import sys

import config
import nicehash.api
import devices
from units import *
import nvidia.devices
import stats.nvidia
from stats.profitability import ProfitabilityStats
import utils.shell as shell
from miner_manager import MinerManager


def run_miner(name):
    activeAlgorithm = name
    print("run miner for: ", name)

def delimiter():
    print()
    print("=" * 100)
    print()

def check():
    nicehashstats = nicehash.api.getCurrentStats()

    s = ProfitabilityStats(gpuType, gpuCount)
    s.print(nicehashstats, limit=5, header=False)
    print()

    return s.calculate(nicehashstats)

if __name__ == "__main__":
    activeAlgorithm = None

    gpuType = devices.NiceHashGTX1080Ti()
    gpuCount = nvidia.devices.numberOfGPUs()
    
    manager = MinerManager()
    
    print("Starting niceminer...")
    print("Supported algs: ", manager.supported())
    print("Found %d GPUs" % gpuCount)
    stats.nvidia.printGPUs()

    while True:
        delimiter()
        stats = check()
        manager.update(stats)

        if manager.alg_switched:
            time.sleep(config.minimum_time_for_running_alg)

        time.sleep(config.check_profitability_interval)
    
