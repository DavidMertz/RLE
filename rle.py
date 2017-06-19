# module: rle

from itertools import repeat, chain, groupby

def rle_encode(it):
    return ((k, len(list(g))) for k, g in groupby(it))

def rle_decode(it):
    return chain.from_iterable(repeat(x, n) for x, n in it)


if __name__ == "__main__":
    orig = [1,1,1,1,2,3,4,4,3,3,3]
    rle = [(1, 4), (2, 1), (3, 1), (4, 2), (3, 3)]
    assert list(rle_encode(orig)) == rle
    assert list(rle_decode(rle)) == orig

