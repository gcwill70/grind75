from balanced_binary_tree.balanced_binary_tree import Solution


def test1():
    assert Solution().isValidBST(None) == True


def test2():
    assert Solution().isValidBST([2, 1, 3]) == True


def test3():
    assert Solution().isValidBST([5, 1, 4, None, None, 3, 6]) == False
