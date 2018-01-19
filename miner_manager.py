import config
from miner_thread import MinerThread

from algs.nist5 import Nist5
from algs.blake2s import Blake2s
from algs.equihash import Equihash
from algs.keccak import Keccak
from algs.lyra2rev2 import Lyra2REv2


class MinerManager:
    def __init__(self):
        self.current_alg = None
        self.stats = None
        self.alg_switched = False
        self.miner_thread = None

        self.supported_miners = {
            "Nist5": Nist5(),
            "Blake2s": Blake2s(),
            "Keccak": Keccak(),
            "Equihash": Equihash(),
            "Lyra2REv2": Lyra2REv2()
        }

    def supported(self):
        return list(self.supported_miners.keys())

    def filterOnlySupported(self, stats):
        res = []
        for s in stats:
            if s[0] in self.supported_miners:
                res.append(s)
        return res

    def update(self, stats):
        self.stats = self.filterOnlySupported(stats)
        print(self.stats)
        self.alg_switched = False
        most_profitable = self.stats[0][0]

        if self.current_alg is None:
            self.run(most_profitable)
        elif self.current_alg != most_profitable:
            print("Profitability diff: ", self.__profitabilityDiff(most_profitable))
            if config.change_alg_when_difference_is_bigger_then < self.__profitabilityDiff(most_profitable):
                self.run(most_profitable)
            else:
                print("not switching yet")
        else:
            print("continue with current miner")

    def run(self, name):
        print("Change miner: ", self.current_alg, " -> ", name)

        if self.miner_thread is not None:
            print("active = false and join")
            self.miner_thread.active = False
            self.miner_thread.join()
            self.miner_thread = None
            print("exited")

        self.miner_thread = MinerThread(self.supported_miners[name])
        self.miner_thread.start()
        self.current_alg = name
        self.alg_switched = True


    def current_profitability(self):
        if self.current_alg is None:
            return 0

        return self.__getAlgStats(self.current_alg)[1]
        
    def __getAlgStats(self, name):
        for s in self.stats:
            if s[0] == name:
                return s

    def __profitabilityDiff(self, potential_alg):
        current_profitability = self.current_profitability()
        new_profitability = self.__getAlgStats(potential_alg)[1]

        return new_profitability / current_profitability - 1

