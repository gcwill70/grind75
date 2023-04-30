from min_domino_rotations import Solution


def test1():
    assert Solution().minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]) == 2


def test2():
    assert Solution().minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]) == -1


def test3():
    assert (
        Solution().minDominoRotations(
            [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]
        )
        == 0
    )
