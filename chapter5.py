# 5.1
def test_1():
    assert (dutch([0, 1, 2, 0, 2, 1, 1], 1) == [0, 0, 1, 1, 1, 2, 2])
    assert (dutch([2, 1, 2, 2, 2, 2, 2], 1) == [1, 2, 2, 2, 2, 2, 2])
    assert (dutch([0, 1, 0, 0, 0, 0, 0], 1) == [0, 0, 0, 0, 0, 0, 1])
    assert (dutch([2, 2, 1, 0, 0, 0, 0], 2) == [0, 0, 0, 0, 1, 2, 2])


def dutch(arr, i):
    pivot = arr[i]
    a = 0
    b = len(arr) - 1
    current = 0
    while current <= b:
        if arr[current] < pivot:
            # if current == a:
            #    a += 1
            #    current += 1 # we don't need this we can always swap without a problem
            # else: swap with itself is okay and we can move current ahead as well
            # because the element we just swapped into current is equal to the pivot
            arr[a], arr[current] = arr[current], arr[a]
            a += 1
            current += 1
        elif arr[current] > pivot:
            # if current == b:
            #    b -= 1
            #    current += 1
            # else:
            arr[b], arr[current] = arr[current], arr[b]
            b -= 1
        else:
            current += 1
    return arr


# 5.1 Variant 1
def test_group_keys():
    assert (group_keys([0, 1, 2, 0, 2, 1, 1]) == [0, 0, 1, 1, 1, 2, 2])
    assert (group_keys([3, 4, 2, 2, 3, 2, 4]) == [3, 3, 4, 4, 2, 2, 2])


def group_keys(array):
    keys = [None, None, None]
    next_open_key = 0
    a = 0
    b = len(array) - 1
    i = 0
    while i <= b:
        if array[i] not in keys:
            keys[next_open_key] = array[i]
            next_open_key += 1
        if array[i] == keys[0]:
            array[a], array[i] = array[i], array[a]
            # if i == a: i += 1 So the trick is that we don't need this if here
            # An element that is at position a that we skipped earlier has to be
            # equal to the pivot or the middle key in this case.
            i += 1
            a += 1
        elif array[i] == keys[1]:
            i += 1
        else:
            array[b], array[i] = array[i], array[b]
            b -= 1
    return array


# 5.1 Variant 2
def test_group_four_keys():
    assert (group_four_keys([0, 2, 1, 1, 3, 2, 3, 0]) == [0, 0, 1, 1, 3, 3, 2, 2])


def group_four_keys(array):
    a = 1
    i = 1
    elem = array[0]
    while i < len(array):
        if array[i] == elem:
            array[i], array[a] = array[a], array[i]
            a += 1
        i += 1
    array[a:] = group_keys(array[a:])  # this is not O(1) space anymore since slicing
    # creates a new list, but it's close enough, if you copy and paste the group_key
    # code it is O(1)
    return array


# 5.1 Variant 3 (DOES NOT WORK FOR VARIANT 4)
def test_group_boolean():
    assert (group_boolean([(False, 1), (False, 2), (True, 3),
                           (False, 4), (True, 5), (True, 6)]) ==
            [(False, 1), (False, 2), (False, 4), (True, 3), (True, 5), (True, 6)])


def group_boolean(array):
    a = 0
    for i in range(len(array)):
        if not array[i][0]:
            array[i], array[a] = array[a], array[i]
            a += 1
    return array


# 5.1 Variant 4
def test_group_boolean_ordered():
    assert (group_boolean_ordered([(False, 1), (True, 2), (False, 3),
                                   (True, 4), (False, 5), (True, 6)]) ==
            [(False, 1), (False, 5), (False, 3), (True, 2), (True, 4), (True, 6)])


def group_boolean_ordered(array):
    b = len(array) - 1
    i = len(array) - 1
    while i >= 0:
        if array[i][0]:
            print(i, b)
            array[i], array[b] = array[b], array[i]
            b -= 1
        i -= 1
    return array


# 5.2
def test_f():
    assert (increment_integer([1, 2, 9]) == [1, 3, 0])
    assert (increment_integer([1]) == [2])
    assert (increment_integer([9, 9]) == [1, 0, 0])


def increment_integer(lst):
    i = len(lst) - 1
    nine = False
    while i >= 0:
        if lst[i] == 9:
            lst[i] = 0
            i -= 1
            nine = True
        else:
            break
    if i == -1 and nine:
        lst = [0] + lst
        i += 1
    lst[i] += 1
    return lst


# 5.2 Variant

def test_g():
    assert (add_binary('11', '10') == '101')
    assert (add_binary('111', '10') == '1001')


def add_binary(s, t):
    i = len(s) - 1
    j = len(t) - 1
    carry = 0
    new = []
    while i >= 0 or j >= 0 or carry:
        x = 0

        if i >= 0 and s[i] == '1':
            x += 1
        if j >= 0 and t[j] == '1':
            x += 1
        x += carry
        new = [str(x % 2)] + new
        carry = x // 2
        i -= 1
        j -= 1

    return "".join(new)


# 5.3
def test_h():
    assert (multiply_better([1, 2], [1, 2]) == [1, 4, 4])
    assert (multiply_better([1, 9, 3, 7, 0, 7, 7, 2, 1],
                            [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]) ==
            [-1, 4, 7, 5, 7, 3,
             9, 5, 2, 5, 8, 9, 6,
             7, 6, 4, 1, 2, 9, 2,
             7])


def multiply(x, y):
    neg = 1
    if x[0] < 0 and y[0] < 0:
        x[0] *= -1
        y[0] *= -1
    elif x[0] < 0:
        x[0] *= -1
        neg = -1
    elif y[0] < 0:
        y[0] *= -1
        neg = -1

    r = []

    def add_to_ret(ret, z):
        i = len(z) - 1
        j = len(ret) - 1
        carry = 0
        while i >= 0 or carry > 0:
            if j < 0:
                j += 1
                ret = [0] + ret

            sm = (z[i] if i >= 0 else 0) + ret[j] + carry
            if sm >= 10:
                carry = 1
                sm -= 10
            else:
                carry = 0
            ret[j] = sm

            i -= 1
            j -= 1
        return ret

    a = len(x) - 1
    a_tens = 0
    while a >= 0:
        b = len(y) - 1
        b_tens = 0
        while b >= 0:
            mult = x[a] * y[b]
            mult_list = [0 for _ in range(a_tens + b_tens)]
            while mult > 0:
                mult_list = [mult % 10] + mult_list
                mult //= 10
            r = add_to_ret(r, mult_list)
            b_tens += 1
            b -= 1
        a_tens += 1
        a -= 1

    r[0] *= neg
    return r


def multiply_better(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            print(i, j)
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
    # Remove the leading zeroes,
    result = result[next((i for i, x in enumerate(result)
                          if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


# 5.4
def test_i():
    assert (advance_better([3, 3, 1, 0, 2, 0, 1]) == True)
    assert (advance_better([3, 2, 0, 0, 2, 0, 1]) == False)


def advance(array):
    possible = [0 for _ in range(len(array))]
    possible[0] = 1
    for i, a in enumerate(array):
        if possible[i] == 1:
            for j in range(i + 1, i + a + 1):
                if j == len(array):
                    break
                possible[j] = 1
    return possible[-1] == 1


def advance_better(array):
    farthest = 0
    for i in range(len(array)):
        if i > farthest:
            break
        farthest = max(farthest, i + array[i])

    return farthest >= len(array) - 1


# 5.4 Variant

def test_j():
    assert (min_steps_to_advance([3, 3, 0, 2, 1, 0]) == 2)
    assert (min_steps_to_advance_better([3, 3, 0, 2, 1, 0]) == 2)


def min_steps_to_advance(array):
    min_steps = [float('inf') for _ in array]
    min_steps[0] = 0
    for i, a in enumerate(array[:-1]):
        for j in range(i + 1, i + a + 1):
            if j == len(array):
                break
            min_steps[j] = min(min_steps[j], min_steps[i] + 1)
    return min_steps[-1]


def min_steps_to_advance_better(array):
    steps = 0
    farthest = 0
    farthest_in_current_steps = 0
    for i, a in enumerate(array[:-1]):
        if i > farthest:
            return -1

        farthest = max(farthest, i + a)
        if i == farthest_in_current_steps:
            farthest_in_current_steps = farthest
            steps += 1
    return steps


# 5.5

def test_k():
    assert (delete_duplicates([2, 3, 5, 5, 7, 11, 11, 11, 13]) == [2, 3, 5, 7, 11, 13, 0, 0, 0])


def delete_duplicates(array):
    next_open = 1
    last = array[0]
    for i, a in list(enumerate(array))[1:]:
        if a != last:
            array[next_open] = a
            last = a
            next_open += 1
    for i in range(next_open, len(array)):
        array[i] = 0
    return array


# 5.5 Variant

def test_l():
    array = [5, 3, 1, 2, 3, 2, 5, 6]
    assert (remove_key(array, 3) == 2)
    assert (array == [5, 6, 1, 2, 5, 2, 5, 6])

    array = [5, 3, 1, 2, 3, 2, 5, 3]
    assert (remove_key(array, 3) == 3)
    assert (array == [5, 5, 1, 2, 2, 2, 5, 3])

    array = [5, 3, 1, 2, 3, 2, 5, 6]
    assert (remove_key_better(array, 3) == 2)
    assert (array == [5, 1, 2, 2, 5, 6, 5, 6])

    array = [5, 3, 1, 2, 3, 2, 5, 3]
    assert (remove_key_better(array, 3) == 3)
    assert (array == [5, 1, 2, 2, 5, 2, 5, 3])


def remove_key(array, key):
    i = 0
    j = len(array) - 1
    while i <= j:
        if array[i] == key:
            array[i] = array[j]
            j -= 1
        else:
            i += 1

    return (len(array) - j) - 1


def remove_key_better(array, key):  # Actually correct implementation that shifts
    open_index = 0
    for i in range(len(array)):
        if array[i] != key:
            array[open_index] = array[i]
            open_index += 1
        i += 1
    return len(array) - open_index


# 5.5 Variant 2

def test_weird():
    assert (weird([1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6], 3) == [1, 2, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6])
    assert (weird([1, 1, 1, 1, 2, 2, 2, 3, 3], 4) == [1, 1, 2, 2, 2, 3, 3, 3, 3])
    assert (weird([3, 3, 3], 3) == [3, 3, None])  # my guess is None should be added here


def weird(array, m):
    if m == 1 or m == 2:
        return array
    last = array[0]
    occ = 1
    last_open = 1
    for i, a in enumerate(array):
        if i == 0:
            continue
        if a == last:
            occ += 1
        else:
            if occ == m:
                last_open -= (m - 2)
            occ = 1
            last = a
        array[last_open] = a
        last_open += 1
    if occ == m:
        last_open -= (m - 2)
        for i in range(last_open, len(array)):
            array[i] = None
    return array


# 5.6
def test_stock():
    assert (stock([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 30)
    assert (stock([300, 350, 250, 260, 330]) == 80)


def stock(array):
    mn = array[0]
    best = 0
    for a in array[1:]:
        if a < mn:
            mn = a
        elif a - mn > best:
            best = a - mn
    return best


# 5.6 Variant 1
def test_longest_subarray():
    assert (longest_subarray([5, 5, 3, 3, 3, 1, 3, 1, 4, 4]) == 3)


def longest_subarray(array):
    occ = 1
    current = array[0]
    longest = 1
    for a in array[1:]:
        if a != current:
            longest = max(occ, longest)
            current = a
            occ = 1
        else:
            occ += 1
    longest = max(occ, longest)
    return longest


# 5.7
def test_stock_twice():
    assert (stock_twice([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 55)
    assert (stock_twice([12, 11, 13, 9, 12, 8, 14, 13, 15]) == 10)


def stock_twice(array):
    mn = array[0]
    sell_by = [0 for _ in array]
    for i, a in list(enumerate(array))[1:]:
        sell_by[i] = max(sell_by[i - 1], a - mn)
        mn = min(mn, a)

    mx = array[-1]
    ret = float('-inf')
    for i, a in reversed(list(enumerate(array))):
        ret = max(ret, mx - a + (sell_by[i - 1] if i != 0 else 0))
        mx = max(mx, a)
    return ret


# 5.7 Variant 1
def test_stock_twice_variant():
    assert (stock_twice_variant([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]) == 55)
    assert (stock_twice_variant([12, 11, 13, 9, 12, 8, 14, 13, 15]) == 10)


def stock_twice_variant(array):
    min_price_so_far = array[0]
    max_profit_after_first_sell = float('-inf')
    max_profit_after_buyback = float('-inf')
    max_profit = float('-inf')

    for a in array[1:]:
        max_profit = max(max_profit, max_profit_after_buyback + a)
        max_profit_after_buyback = max(max_profit_after_buyback, max_profit_after_first_sell - a)
        max_profit_after_first_sell = max(max_profit_after_first_sell, a - min_price_so_far)
        min_price_so_far = min(min_price_so_far, a)
    return max_profit


# 5.8
def test_alternating():
    array = [3, 1, 5, 6, 2, 6, 3, 6, 2, 3]
    ret = alternating(array)
    print(ret)
    for i in range(len(ret))[::2]:
        assert (ret[i] <= ret[i + 1])
    for i in range(len(ret))[1::2]:
        assert (ret[i] >= ret[i - 1])


def alternating(array):
    mod = 1
    for i in range(len(array))[1:]:
        if mod == 1:
            if array[i] < array[i - 1]:
                array[i - 1], array[i] = array[i], array[i - 1]
        else:
            if array[i] > array[i - 1]:
                array[i - 1], array[i] = array[i], array[i - 1]
        mod = 1 - mod
    return array


# 5.9
def test_primes():
    assert (primes(15) == [2, 3, 5, 7, 11, 13])
    assert (primes(9) == [2, 3, 5, 7])
    assert (primes(23) == [2, 3, 5, 7, 11, 13, 17, 19, 23])


import math


def primes(n):
    ret = list()
    is_prime = [1 for i in range(0, n + 1)]
    for i in range(2, math.floor(math.sqrt(n) + 1)):
        if is_prime[i]:
            ret.append(i)
        j = 2
        while i * j < n + 1:
            is_prime[i * j] = 0
            j += 1
    for i in range(math.floor(math.sqrt(n) + 1), n + 1):
        if is_prime[i]:
            ret.append(i)
    return ret


# 5.10
def test_apply_permutation():
    assert (apply_permutation([1, 2, 3, 4], [2, 0, 1, 3]) == [2, 3, 1, 4])
    assert (apply_permutation([1, 2, 3, 4], [1, 0, 3, 2]) == [2, 1, 4, 3])


def apply_permutation(A, P):
    visited = [False for _ in A]
    for A_index in range(len(A)):
        if visited[A_index]:
            continue
        to_be_swapped = A_index
        visited[A_index] = True
        while P[to_be_swapped] != A_index:
            visited[P[to_be_swapped]] = True
            A[A_index], A[P[to_be_swapped]] = A[P[to_be_swapped]], A[A_index]
            to_be_swapped = P[to_be_swapped]
    return A


# 5.10 Variation

def test_inverse_permutation():
    assert (inverse_permutation([1, 2, 3, 4], [2, 0, 1, 3]) == [3, 1, 2, 4])
    assert (inverse_permutation([1, 2, 3, 4], [1, 0, 3, 2]) == [2, 1, 4, 3])
    assert (inverse_permutation([1, 2, 3, 4], [1, 2, 3, 0]) == [2, 3, 4, 1])


def inverse_permutation(A, P):
    visited = [False for _ in A]
    for A_index in range(len(A)):
        if visited[A_index]:
            continue
        visited[A_index] = True
        current = P[A_index]
        prev = A_index
        while current != A_index:
            visited[current] = True
            A[prev], A[current] = A[current], A[prev]
            prev = current
            current = P[current]
    return A


# 5.11
def test_next_permutation():
    assert (next_permutation([0, 1, 2]) == [0, 2, 1])
    assert (next_permutation([1, 0, 2]) == [1, 2, 0])
    assert (next_permutation([2, 0, 1]) == [2, 1, 0])
    assert (next_permutation([2, 1, 0]) == [])
    assert (next_permutation([1, 5, 4, 3, 2]) == [2, 1, 3, 4, 5])
    assert (next_permutation([2, 5, 4, 3, 1]) == [3, 1, 2, 4, 5])


def next_permutation(array):
    i = len(array) - 2
    while i >= 0:
        if array[i] < array[i + 1]:
            j = len(array) - 1
            for j in reversed(range(len(array))):
                if array[j] > array[i]:
                    array[i], array[j] = array[j], array[i]
                    # array[i + 1:] = sorted(array[i + 1:])
                    array[i + 1:] = reversed(array[i + 1:])  # just reversing is enough
                    return array
        i -= 1
    return []


# 5.11 Variant 1
def test_kth_permutation():
    assert (kth_permutation(5, 4) == [0, 1, 4, 2, 3])
    assert (kth_permutation(3, 4) == [2, 0, 1])
    # 0, 1, 2, 3 ,4
    # 0, 1, 2, 4, 3
    # 0, 1, 2, 3 ,4 PREV (2) * 2
    # 0, 1, 2, 4, 3
    # 3 * PREV
    # 4 * PREV
    # 2, 2*(2), 3*(2*2), 4*3*(2*2)


def kth_permutation(n, k):
    ret = []
    elements = list(range(0, n))
    remaining = k
    for i in range(n - 1, -1, -1):
        elem = elements[remaining // math.factorial(i)]
        remaining = remaining % math.factorial(i)
        ret.append(elem)
        elements.remove(elem)
    return ret


# 5.11 Variant 2
def test_previous_permutation():
    assert (previous_permutation([0, 1, 2]) == [])
    assert (previous_permutation([2, 0, 1]) == [1, 2, 0])
    assert (previous_permutation([2, 1, 0]) == [2, 0, 1])
    assert (previous_permutation([1, 2, 0]) == [1, 0, 2])


def previous_permutation(perm):
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] > perm[i + 1]:
            # Found the right place to swap
            for j in range(len(perm) - 1, 0, -1):
                if perm[j] < perm[i]:
                    perm[i], perm[j] = perm[j], perm[i]
                    perm[i + 1:] = reversed(perm[i + 1:])
                    return perm

    return []


# 5.12
def test_random_subset():
    for _ in range(5):
        print(random_subset(list(range(10)), 3))
    assert True


import random


def random_subset(array, size):
    last = len(array) - 1
    subset = []
    for _ in range(size):
        i = random.randint(0, last)
        subset.append(array[i])
        array[i], array[last] = array[last], array[i]
        last -= 1
    return subset


# 5.12 Variant 1
# No it does not, unless n-1 is a multiple of RAND_MAX-1.

# 5.13
import itertools


# the chance of a packet being in a random subset is k/n
# through the formula (n-1 C k-1) / (n C k)
# so take a random subset of size k-1 and conditionally
# adding in the new packet should produce the same
# probability space
def uniform_packets_subset(it, k):
    random_subset2 = list(itertools.islice(it, k))

    packets_seen = k
    for x in it:
        packets_seen += 1
        r = random.randrange(0, packets_seen)
        if r < k:
            random_subset2[r] = x
    return random_subset2


# 5.14

# 5.17
def test_sudoku():
    board = []
    board += [5, 3, 0, 0, 7, 0, 0, 0, 0]
    board += [6, 0, 0, 1, 9, 5, 0, 0, 0]
    board += [0, 9, 8, 0, 0, 0, 0, 6, 0]
    board += [8, 0, 0, 0, 6, 0, 0, 0, 3]
    board += [4, 0, 0, 8, 0, 3, 0, 0, 1]
    board += [7, 0, 0, 0, 2, 0, 0, 0, 6]
    board += [0, 6, 0, 0, 0, 0, 2, 8, 0]
    board += [0, 0, 0, 4, 1, 9, 0, 0, 5]
    board += [0, 0, 0, 0, 8, 0, 0, 7, 9]

    sol = []
    sol += [5, 3, 4, 6, 7, 8, 9, 1, 2]
    sol += [6, 7, 2, 1, 9, 5, 3, 4, 8]
    sol += [1, 9, 8, 3, 4, 2, 5, 6, 7]
    sol += [8, 5, 9, 7, 6, 1, 4, 2, 3]
    sol += [4, 2, 6, 8, 5, 3, 7, 9, 1]
    sol += [7, 1, 3, 9, 2, 4, 8, 5, 6]
    sol += [9, 6, 1, 5, 3, 7, 2, 8, 4]
    sol += [2, 8, 7, 4, 1, 9, 6, 3, 5]
    sol += [3, 4, 5, 2, 8, 6, 1, 7, 9]

    # assert (sudoku(board) == sol)
    # assert (valid_sudoku(sol))


def sudoku(board):
    sol = []
    rows_avail = []
    cols_avail = []
    square_avail = {}
    for row in range(9):
        rows_avail.append(set(1, 2, 3, 4, 5, 6, 7, 8, 9) - set(board[row]))
    for col in range(9):
        cols_avail.append(set(1, 2, 3, 4, 5, 6, 7, 8, 9) - set([board[row][col] for row in range(9)]))
    for sq in range(9):
        row_sq = sq // 3
        col_sq = sq % 3
        square_avail[(row_sq, col_sq)] = set(1, 2, 3, 4, 5, 6, 7, 8, 9) - set([
            board[row][col]
            for row in range(row_sq * 3, row_sq * 3 + 3)
            for col in range(col_sq * 3, col_sq * 3 + 3)
        ])
    for row in range(9):
        for col in range(9):
            if (realValue := board[row][col]) != 0:
                sol[row][col] = [realValue]
            else:
                sol[row][col] = rows_avail[row].intersection(cols_avail[col]).intersection(
                    square_avail[(row // 3, col % 3)])

    # AND I was trying to solve it lol
    # for row in range(9):
    #    for col in range(9):
    #        sol[row][col] = set(1, 2, 3, 4, 5, 6, 7, 8, 9) if board[row][col] == 0 else board[row][col]

    # for row in range(9):
    #    s = set(sol[row])
    #    for col in range(9):
    #        if type(sol[row][col]) == set:
    #            sol[row][col] -= s

    return sol
