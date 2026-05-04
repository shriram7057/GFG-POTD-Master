class Solution:
    def isBinaryPalindrome(self, n):
        b = bin(n)[2:]
        return b == b[::-1]