import random

# https://leetcode.com/problems/insert-delete-getrandom-o1
class RandomizedSet:

    def __init__(self):
        self.s = []
        self.m = {}
        self.idx = -1

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.m:
            return False
        self.idx += 1
        self.s.append(val)
        self.m[val] = self.idx
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.m:
            tmp = self.m[val]
            last = self.s[-1]
            self.s[tmp] = last
            self.m[last] = tmp
            self.s.pop()
            del self.m[val]
            self.idx -= 1
            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.s[random.randint(0, len(self.s) - 1)]
