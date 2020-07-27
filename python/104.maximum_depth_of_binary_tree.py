# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if root is None else max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
