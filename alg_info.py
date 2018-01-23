from algs.blake2s import Blake2s
from algs.equihash import Equihash
from algs.keccak import Keccak
from algs.lyra2rev2 import Lyra2REv2
from algs.nist5 import Nist5

print(" ".join(Blake2s().getParams()))
print(" ".join(Equihash().getParams()))
print(" ".join(Keccak().getParams()))
print(" ".join(Lyra2REv2().getParams()))
print(" ".join(Nist5().getParams()))