import unittest
def _min(f):
    minn = f[0]
    for i in f:
        if i < minn:
            minn = i
    return minn


def _max(f):
    maxx = f[0]
    for i in f:
        if i > maxx:
            maxx = i
    return maxx


def _sum(f):
    summ = 0
    for i in f:
        summ += i
    return summ


def _mult(f):
    mul = 1
    for i in f:
        mul *= i
    return mul
