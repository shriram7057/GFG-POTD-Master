class Solution:
	def distinctSubseq(self, str):
		# code here
		mod = 10**9 + 7
		n =len(str)
		
		dp = [0] * (n + 1)
		dp[0] = 1
		
		last={}
		for i in range(1,n+1):
		    dp[i] = (dp[i-1]*2) % mod
		    ch = str[i-1]
		    
		    if ch in last:
		        dp[i] = (dp[i] - dp[last[ch] - 1]) % mod
		    last[ch] = i
		return dp[n] % mod