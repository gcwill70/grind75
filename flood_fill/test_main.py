from main import Solution


def test1():
    assert Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]


def test2():
    assert Solution().floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1) == [
        [0, 0, 0],
        [0, 1, 1],
    ]
