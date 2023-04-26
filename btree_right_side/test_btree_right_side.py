from btree_right_side.btree_right_side import Solution
from utils.treenode import TreeNode


def test1():
    assert Solution().rightSideView(TreeNode.fromList([1, 2, 3, None, 5, None, 4])) == [
        1,
        3,
        4,
    ]


def test2():
    assert Solution().rightSideView(TreeNode.fromList([1, None, 3])) == [1, 3]


def test3():
    assert Solution().rightSideView(TreeNode.fromList([])) == []
