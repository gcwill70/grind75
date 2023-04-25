from subsets.subsets import Solution


def test1():
    assert Solution().subsets([1, 2, 3]) == [
        [],
        [1],
        [2],
        [1, 2],
        [3],
        [1, 3],
        [2, 3],
        [1, 2, 3],
    ]


def test2():
    assert Solution().subsets([0]) == [[], [0]]
