class Solution:
    def isBitSet(self, n):
        return n != 0 and (n & (n + 1)) == 0