from three_sum.three_sum import Solution


def test1():
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


def test2():
    assert Solution().threeSum([]) == []


def test3():
    assert Solution().threeSum([0]) == []


def test4():
    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]


def test5():
    assert Solution().threeSum([0, 0, 0, 0]) == [[0, 0, 0]]


def test6():
    assert Solution().threeSum([1, 2, -2, -1]) == [[1, 2, -2, -1]]
