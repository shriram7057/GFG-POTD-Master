class Solution:
    def getLastMoment(self, n, left, right):
        # code here
        ans = 0
        if left:
            ans = max(ans,max(left))
        if right:
            ans = max(ans,n - min(right))
        return ans