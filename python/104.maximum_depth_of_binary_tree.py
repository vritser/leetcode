from typedef.treenode import TreeNode

# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if root is None else max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
