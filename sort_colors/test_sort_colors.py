from sort_colors.sort_colors import Solution


def test1():
    assert Solution().sortColors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]


def test2():
    assert Solution().sortColors([2, 0, 1]) == [0, 1, 2]
