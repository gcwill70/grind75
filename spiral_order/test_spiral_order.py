from spiral_order.spiral_order import Solution


def test1():
    assert Solution().spiralOrder(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    ) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test2():
    assert Solution().spiralOrder(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ]
    ) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
