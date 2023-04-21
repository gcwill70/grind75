from utils.treenode import TreeNode
from valid_bst.valid_bst import Solution


def test1():
    assert Solution().isValidBST(None) == True


def test2():
    assert Solution().isValidBST(TreeNode.fromList([2, 1, 3])) == True


def test3():
    assert (
        Solution().isValidBST(TreeNode.fromList([5, 1, 4, None, None, 3, 6])) == False
    )


def test4():
    assert (
        Solution().isValidBST(TreeNode.fromList([5, 4, 6, None, None, 3, 7])) == False
    )
