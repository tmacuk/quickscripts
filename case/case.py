import sys

word = sys.argv[1]

from itertools import product
def randString(istr):
    l = [(c, c.upper()) if not c.isdigit() else (c,) for c in istr.lower()]
    return ["".join(item) for item in product(*l)]

print randString(word)
