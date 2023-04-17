from climbing_stairs.climbing_stairs import Solution


def test1():
    assert Solution().climbStairs(1) == 1


def test2():
    assert Solution().climbStairs(2) == 2


def test3():
    assert Solution().climbStairs(3) == 3


def test4():
    assert Solution().climbStairs(4) == 5


def test5():
    assert Solution().climbStairs(5) == 8


def test6():
    assert Solution().climbStairs(6) == 13


def test7():
    assert Solution().climbStairs(7) == 21


def test8():
    assert Solution().climbStairs(8) == 34
