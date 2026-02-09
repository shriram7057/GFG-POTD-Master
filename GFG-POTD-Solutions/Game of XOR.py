class Solution:
    def subarrayXor(self, arr):
        # code here 
        n=len(arr)
        ans=0
        for i in range(n):
            freq=(i+1) * (n-i)
            if freq % 2 ==1:
                ans ^= arr[i]
        return ans