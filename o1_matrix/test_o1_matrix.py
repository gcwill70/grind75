from o1_matrix.o1_matrix import Solution


def test1():
    assert Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]


def test2():
    assert Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]) == [
        [0, 0, 0],
        [0, 1, 0],
        [1, 2, 1],
    ]


def test3():
    assert Solution().updateMatrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == [
        [2, 1, 2],
        [1, 2, 1],
        [2, 1, 2],
    ]


def test4():
    assert Solution().updateMatrix([[1, 1, 1], [1, 1, 1], [1, 1, 0]]) == [
        [2, 1, 2],
        [1, 2, 1],
        [0, 1, 0],
    ]


def test5():
    assert Solution().updateMatrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == [
        [2, 1, 2],
        [1, 2, 1],
        [2, 1, 2],
    ]
