from utils.treenode import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        lenLeft = self.__getHeight__(root.left, 0)
        lenRight = self.__getHeight__(root.right, 0)
        return (
            abs(lenLeft - lenRight) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def __getHeight__(self, root: TreeNode, height: int) -> int:
        if root == None:
            return height
        height += 1
        print(f"__getHeight__\ntree:{root.print()}\nheight:{height}\n\n")
        return max(
            self.__getHeight__(root.left, height),
            self.__getHeight__(root.right, height),
        )
