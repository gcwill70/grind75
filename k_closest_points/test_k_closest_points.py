from k_closest_points.k_closest_points import Solution


def test1():
    assert Solution().kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]


def test2():
    assert Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[-2, 4], [3, 3]]


def test3():
    assert Solution().kClosest([[0, 1], [1, 0]], 2) == [[0, 1], [1, 0]]
