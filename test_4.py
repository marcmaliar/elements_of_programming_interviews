import uuid

words = [6914104489697087981, 6914105048042836461,
         6914105176891855341, 6914105262791201261]


# class TestClass:

# def test_4_1(self):
#    assert (func() == 1)


def random64():
    return uuid.uuid1().int >> 64


cache = {}


def parity(x, shift):
    if x in cache:
        return cache[x]
    y = x >> shift
    p = parity(y)


def func(l):
    return [cache[x] for x in l]
