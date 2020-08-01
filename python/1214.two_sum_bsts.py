from typedef.treenode import TreeNode
from typing import Set

# https://leetcode.com/problems/two-sum-bsts/
class Solution:
    def twoSumBSTs(self, r1: TreeNode, r2: TreeNode, target: int) -> bool:
        def preorder(root: TreeNode, s: Set[int]) -> None:
            if not root: return
            s.add(root.val)
            preorder(root.left)
            preorder(root.right)

        def exists(root: TreeNode, s: Set[int], target: int) -> bool:
            if not root: return False
            if (target - root.val) in s:
                return True

            return exists(root.left, s, target) or exists(root.right, s, target)

        s = set()
        preorder(r1, s)
        return exists(r2, s, target)
