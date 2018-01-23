import nicehash.algorithms
import logging

class ProfitabilityStats: 
    def __init__(self, gpuType, gpuCount):
        self.__gpu = gpuType
        self.__gpuCount = gpuCount

    def print(self, nicehash_stats, header = True, limit = -1):
        logger = logging.getLogger()  
        sorted_stats = self.calculate(nicehash_stats)

        if limit != -1:
            sorted_stats = sorted_stats[:limit]

        if header:
            header = ["Algorithm", "1 GPU/Day", "1 GPU/Month", "%d GPU/day" % self.__gpuCount, "%d GPU/month" % self.__gpuCount]
            logger.info("{: >15} {: >14} {: >14} {: >14} {: >14}".format(*header))
            logger.info("-" * 75)
        
        for a in sorted_stats:
            logger.info("{: >15} {: >14f} {: >14f} {: >14f} {: >14f}".format(*a))
        

    
    def calculate(self, nicehash_stats, limit = -1):
        out = self.__process(nicehash_stats)
        arr = list(self.__sort(out))
        
        if limit == -1:
            return arr
        
        return arr[:limit]



    def __process(self, nicehash_stats):
        res = []
        for alg in nicehash_stats:
            if alg[0] in self.__gpu.stats:
                gpuSpeed = self.__gpu.stats[alg[0]]
                perDay = gpuSpeed * alg[1]

                algName = nicehash.algorithms.algoIdToName(alg[0])

                res.append([
                    algName,
                    perDay, 
                    perDay * 31, 
                    perDay * self.__gpuCount,
                    perDay * self.__gpuCount * 31
                ])
        return res

    def __sort(self, statsarr):
        return reversed(sorted(statsarr, key=lambda x: x[1]))
        
