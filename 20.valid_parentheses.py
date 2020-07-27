# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        ps = {
            '(': ')',
            '{' : '}',
            '[': ']'
        }
        stack = []

        for c in s:
            if c in ps:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if ps[stack.pop()] != c:
                    return False
        return len(stack) == 0
