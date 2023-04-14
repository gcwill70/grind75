from balanced_binary_tree.balanced_binary_tree import Solution
from utils.treenode import TreeNode


def test1():
    assert Solution().isBalanced(None) == True


def test2():
    assert Solution().isBalanced([]) == True


def test3():
    assert (
        Solution().isBalanced(TreeNode.fromList([1, 2, 2, 3, 3, None, None, 4, 4]))
        == False
    )


def test4():
    assert (
        Solution().isBalanced(TreeNode.fromList([3, 9, 20, None, None, 15, 7])) == True
    )


def test5():
    assert (
        Solution().isBalanced(
            TreeNode.fromList([1, 2, 2, 3, None, None, 3, 4, None, None, 4])
        )
        == False
    )
