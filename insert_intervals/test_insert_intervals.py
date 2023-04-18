from insert_intervals.insert_intervals import Solution


def test1():
    assert Solution().insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]


def test2():
    assert Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16],
    ]


def test3():
    assert Solution().insert([], [5, 7]) == [[5, 7]]


def test4():
    assert Solution().insert([[1, 5]], [2, 3]) == [[1, 5]]


def test5():
    assert Solution().insert([[1, 5]], [2, 7]) == [[1, 7]]


def test6():
    assert Solution().insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]


def test7():
    assert Solution().insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
