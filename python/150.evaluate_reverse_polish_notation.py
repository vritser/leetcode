# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    op = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(y / x)
    }

    stack = []

    def evalRPN(self, tokens: List[str]) -> int:
        for c in tokens:
            if c in self.op:
                self.stack.append(self.op[c](self.stack.pop(), self.stack.pop()))
            else:
                self.stack.append(int(c))

        return self.stack.pop()
