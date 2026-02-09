class Solution:
    def minCost(self, keys, freq):
        # code here
        n=len(keys)
        prefix = [0] * (n+1)
        
        for i in range(n):
            prefix[i+1] = prefix[i] + freq[i]
            
        def get_sum(i,j):
            return prefix[j+1] - prefix[i]
            
        dp=[[0] * n for _ in range(n)]
        
        for length in range(1 , n+1):
            for i in range(n-length+1):
                j=i+length - 1
                
                dp[i][j]=float('inf')
                
                for r in range(i,j+1):
                    left=dp[i][r-1] if r > i else 0
                    right=dp[r+1][j] if r < j else 0
                    
                    cost = left + right + get_sum(i,j)
                    dp[i][j] = min(dp[i][j],cost)
        return dp[0][n-1]
 