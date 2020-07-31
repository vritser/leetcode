from queue import Queue
from typedef.treenode import TreeNode
from typing import List, Set

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        def find(root: TreeNode, k: int, s: Set[int]) -> bool:
            if root == None: return False

            if (k - root.val) in s:
                return True
            s.add(root.val)

            return find(root.left, k, s) or find(root.right, k, s)

        return find(root, k, s)

    def findTarget2(self, root: TreeNode, k: int) -> bool:
        q = Queue()
        q.put(root)
        s = set()

        while not q.empty():
            n = q.get();

            if (k - n.val) in s:
                return True
            s.add(n.val)

            if n.left:
                q.put(n.left)

            if n.right:
                q.put(n.right)

        return False

    def findTarget3(self, root: TreeNode, k: int) -> bool:
        def inorder(root: TreeNode, ns: List[int]) -> None:
            if not root: return
            inorder(root.left, ns)
            ns.append(root.val)
            inorder(root.right, ns)

        ns = []
        inorder(root, ns)

        l, r = 0, len(ns) - 1

        while l < r:
            sum = ns[l] + ns[r]
            if k == sum:
                return True
            elif k < sum:
                r -= 1
            else:
                l += 1

        return False
