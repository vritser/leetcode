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



class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
