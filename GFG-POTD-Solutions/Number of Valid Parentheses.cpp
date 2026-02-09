class Solution {
  public:
    int findWays(int n) {
        // code here
        if (n%2==1) return 0;
        int pairs = n / 2;
        vector<long long>dp(pairs + 1, 0);
        dp[0] = 1;
        for(int i = 1;i <= pairs;i++)
        {
            for(int j = 0;j < i;j++)
            {
                dp[i] += dp[j] * dp[i - j - 1];
            }
        }
        return dp[pairs];
    }
};