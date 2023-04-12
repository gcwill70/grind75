from main import Solution


def test_first():
    assert Solution().mergeTwoLists([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]


def test_second():
    assert Solution().mergeTwoLists([], []) == []


def test_third():
    assert Solution().mergeTwoLists([], [0]) == [0]
