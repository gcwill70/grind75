from coin_change.coin_change import Solution


def test1():
    assert Solution().coinChange([1, 2, 5], 11) == 3


def test2():
    assert Solution().coinChange([2], 3) == -1


def test3():
    assert Solution().coinChange([1], 0) == 0
