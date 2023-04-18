from max_subarray.max_subarray import Solution


def test1():
    assert Solution().maxSubArray([1]) == 1


def test2():
    assert Solution().maxSubArray([-2, 1]) == 1


def test3():
    assert Solution().maxSubArray([-2, -1]) == -1


def test4():
    assert Solution().maxSubArray([-2, -1, -3]) == -1


def test5():
    assert Solution().maxSubArray([-2, -1, -3, 5]) == 5


def test6():
    assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23


def test7():
    assert Solution().maxSubArray([-2, -1, -3, 5, -4]) == 5


def test8():
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
