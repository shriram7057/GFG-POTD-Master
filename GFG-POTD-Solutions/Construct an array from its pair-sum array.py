class Solution:
    def constructArr(self, arr):
        # code here
        m=len(arr)
        
        import math
        n  = int((1+ math.isqrt(1+8*m)) // 2)
        if n == 2:
            return [0,arr[0]]
        res = [0] * n
        S01 = arr[0]
        S02 = arr[1]
        S12 = arr[n-1]
        
        res[0] = (S01 + S02 - S12) // 2
        res[1] = S01 - res[0]
        res[2] = S02 - res[0]
        
        for i in range(3,n):
            res[i] =arr[i-1] - res[0]
        return res