

def first(x):
    y = x ^ (x-1)
    y >>= 1
    x ^= y
    return x


def second(x, y):
    return x & (y-1)


def third(x):
    return (x & (x-1)) == 0


def fourth(x, i, j):
    if (x >> i & 1) != (x >> j & 1):
        x ^= 1 << i
        x ^= 1 << j
    return x


def fifth_wrong(x):
    i = 0
    j = 0
    while True:
        y = x >> i
        if y & 1 == 0:
            break
        i += 1
    while True:
        y = x >> j
        if y & 1 == 1:
            break
        j += 1
    return x ^ ((1 << i) | (1 << j))


def fifth(x):
    for i in range(63):
        if ((x >> i) & 1) != ((x >> (i+1)) & 1):
            return x ^ ((1 << i) | (1 << (i+1)))

    return None


def fifth_faster(x):
    if x & 1 == 0:
        y = x
    else:
        y = ~x
    lowest = y & ~(y - 1)
    z = lowest | (lowest >> 1)
    return x ^ z


def sixth(x, y):
    # multiply x and y
    sm = 0
    while y != 0:
        yy = y & 1
        xcopy = x

        carry = 0
        sumsum = 0
        factor = 0
        while xcopy != 0:
            xx = xcopy & 1
            s = ((yy & xx) >> 1) + (yy ^ xx)
            ss = s & 1
            s = ((ss & carry) >> 1) + (ss ^ carry)
            carry = s >> 1
            s = s & 1
            sumsum = sumsum | (s << factor)
            factor += 1
            xcopy >>= 1

        if carry == 1:
            sumsum = sumsum | (carry << factor)
        sm += sumsum

        y >>= 1

    return sm


def sixth_better(x, y):
    def add(a, b):
        c = 0
        sm = 0
        k = 1
        tmpa, tmpb = a, b
        while tmpa != 0 or tmpb != 0:
            aa, bb, cc = a & k, b & k, c & k
            digit = aa ^ bb ^ cc
            cin = (aa & bb) | (aa & cc) | (bb & cc)
            sm |= digit
            k <<= 1
            c = cin << 1
            tmpa >>= 1
            tmpb >>= 1
        return sm | c

    s = 0
    while x != 0:
        if x & 1:
            s = add(s, y)
        x >>= 1
        y <<= 1
    return s


def seventh(x, y):
    power = 32
    quot = 0
    while x >= y:
        while y << power > x:
            power -= 1

        quot += 1 << power
        x -= y << power
        power -= 1
    return quot


def eighth(x, y):
    # x^y
    res = 1
    while y != 1:
        if y % 2 == 0:
            x *= x
            y /= 2
        else:
            res *= x
            y -= 1
    return res


class TestClass2:

    def compare(self, f, inp, exp):
        assert (bin(f(int(inp, 2))) == bin(int(exp, 2)))

    def compare2(self, f, inp1, inp2, exp):
        assert (bin(f(int(inp1, 2), int(inp2, 2))) == bin(int(exp, 2)))

    def test_4_2(self):
        assert (first(int("10100000", 2)) == int("10111111", 2))

    def test_4_3(self):
        assert (second(129, 64) == 1)

    def test_4_4(self):
        assert (third(2) == True)
        assert (third(3) == False)
        assert (third(52) == False)
        assert (third(64) == True)

    def test_4_5(self):
        assert (fourth(int("01001001", 2), 1, 6) == int("00001011", 2))

    def test_4_6(self):
        self.compare(fifth, "1011100", "1011010")
        self.compare(fifth, "1011110", "1011101")
        self.compare(fifth, "111", "1011")

    def test_4_7(self):
        self.compare(fifth_faster, "1011100", "1011010")
        self.compare(fifth_faster, "1011110", "1011101")
        self.compare(fifth_faster, "111", "1011")

    def test_4_8(self):
        self.compare2(sixth_better, "10", "10", "100")
        self.compare2(sixth_better, "01101011", "0100010", "111000110110")

    def test_4_8(self):
        self.compare2(seventh, "0101000", "01011", "11")
