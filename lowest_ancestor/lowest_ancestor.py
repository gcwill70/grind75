from utils.treenode import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        while root != None:
            if root.val < small:
                root = root.right
            elif root.val > large:
                root = root.left
            else:
                return root
        return root
