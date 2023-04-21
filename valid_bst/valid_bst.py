import sys
from utils.treenode import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.__isValidBST(root, -sys.maxsize, sys.maxsize)

    def __isValidBST(self, root: TreeNode, minimum, maximum) -> bool:
        if not root:
            return True
        if minimum < root.val < maximum:
            return self.__isValidBST(
                root.left, minimum, root.val
            ) and self.__isValidBST(root.right, root.val, maximum)
        return False
