from algs.blake2s import Blake2s
from algs.equihash import Equihash
from algs.keccak import Keccak
from algs.lyra2rev2 import Lyra2REv2
from algs.nist5 import Nist5

print(" ".join(Blake2s().args))
print(" ".join(Equihash().args))
print(" ".join(Keccak().args))
print(" ".join(Lyra2REv2().args))
print(" ".join(Nist5().args))