class Solution:
    def isPower(self, x, y):
        if y == 1:
            return True
        
        if x == 1:
            return y == 1
        
        while y % x == 0:
            y //= x
        
        return y == 1