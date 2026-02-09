class Solution:
    def areRotations(self, s1, s2):
        # code here
        if len(s1) != len(s2):
            return False
        return s2 in (s1+s1)