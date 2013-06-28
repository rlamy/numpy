from random import Random
from numpy import zeros

_rand = Random()
def random_sample(length=0):
    if length == 0:
        return _rand.random()
    ret = zeros(length)
    for x in xrange(ret.size):
        ret[x] = _rand.random()
    return ret

def randn(length=0):
    if length == 0:
        return _rand.gauss(0., 1.)
    ret = zeros(length)
    for x in xrange(ret.size):
        ret[x] = _rand.gauss(0., 1.)
    return ret

seed = _rand.seed
