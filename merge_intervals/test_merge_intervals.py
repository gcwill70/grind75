from merge_intervals.merge_intervals import Solution


def test1():
    assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]


def test2():
    assert Solution().merge([[1, 4], [4, 5]]) == [[1, 5]]
