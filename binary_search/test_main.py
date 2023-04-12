from main import Solution


def test1():
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4


def test2():
    assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1
