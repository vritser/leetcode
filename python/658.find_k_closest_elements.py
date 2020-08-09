from typing import List

# https://leetcode.com/problems/find-k-closest-elements/
class Solution:
    def findClosestElements(self,  arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = 0, n
        fst, last = arr[0], arr[-1]

        if x < fst:
            return arr[:k]
        if x > last:
            return arr[n - k:]

        while l < r:
            m = (l + r) // 2

            if arr[m] == x:
                break;
            elif arr[m] > x:
                r = m - 1
            else:
                l = m + 1

        begin, end = max(0, m-k-1), min(n-1, m+k+1)

        while (end-begin+1 != k):
            if x-arr[begin] <= arr[end]-x:
                end-=1
            else:
                begin+=1

        return arr[begin: end+1]
