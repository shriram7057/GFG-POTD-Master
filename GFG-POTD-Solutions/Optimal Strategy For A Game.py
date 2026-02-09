class Solution:
    def maximumAmount(self, arr):
        # code here 
        n=len(arr)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = arr[i]
            
        for i in range(n-1):
            dp[i][i+1] = max(arr[i],arr[i+1])
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                
                a=dp[i+2][j] if i+2 <= j else 0
                b=dp[i+1][j-1] if i+1 <= j-1 else 0
                c=dp[i][j-2] if i <= j-2 else 0
                
                take_i =arr[i] + min(dp[i+2][j] if i+2 <= j else 0,
                                     dp[i+1][j-1] if i+1 <= j-1 else 0)
                take_j = arr[j] + min(dp[i+1][j-1] if i+1 <= j-1 else 0,
                                      dp[i][j-2] if i<= j-2 else 0)
                dp[i][j] = max(take_i, take_j)
        return dp[0][n-1]
        