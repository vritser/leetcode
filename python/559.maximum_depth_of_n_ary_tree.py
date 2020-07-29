# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
class Solution:
    def maxDepth(self, root: Node) -> int:
        arr = []
        def depth(root: Node, i: int) -> None:
            if root:
                if i > len(arr):
                    arr.append([])
                arr[i-1].append(root.val)

                for c in root.children:
                    depth(c, i+ 1)
        depth(root, 1)
        return len(arr)

    def maxDepthBottomUp(self, root: Node) -> int:
        if not root: return 0
        if not root.children: return 1

        maxd = 0
        for c in root.children:
            d = 1 + self.maxDepthBottomUp(c)
            if maxd < d:
                maxd = d

        return maxd

    def maxDepthTopDown(self, root: Node) -> int:
        def depth(root: Node, l: int) -> int:
            if not root: return 0
            if not root.children: return l

            maxd = 0
            for c in root.children:
                d = depth(c, l + 1)
                if maxd < d:
                    maxd = d
            return maxd
        return depth(root, 1)



class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
