class Solution:
    def numberOfWays(self, n):
        # Base cases
        if n == 0 or n == 1:
            return 1
        
        # DP array to store number of ways
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        
        # Bottom-up DP without modulo
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
