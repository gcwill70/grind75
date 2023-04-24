from rotting_oranges.rotting_oranges import Solution


def test1():
    assert Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4


def test2():
    assert Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1


def test3():
    assert Solution().orangesRotting([[0, 2]]) == 0
