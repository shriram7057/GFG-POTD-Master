class Solution {
  public:
    int chocolatePickup(vector<vector<int>> &mat) {
        int n = mat.size(),m=mat[0].size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(m, vector<int>(m, -1)));
        
        function<int(int, int, int)> solve = [&](int i, int j1, int j2) -> int {
            if(j1 < 0 || j2 < 0 || j1 >= m || j2 >= m || mat[i][j1] == -1 || mat[i][j2] == -1)
                return -1e9;
            if(i == n - 1)
                return (j1 == j2 ? mat[i][j1] : mat[i][j1] + mat[i][j2]);
            if(dp[i][j1][j2] != -1) return dp[i][j1][j2];
            int ans = -1e9;
            for(int dj1 = -1; dj1 <= 1; ++dj1) {
                for(int dj2 = -1; dj2 <= 1; ++dj2) {
                    int temp = solve(i + 1, j1 + dj1, j2 + dj2);
                    if (temp < 0) continue; // only consider valid paths
                    int val = (j1 == j2 ? mat[i][j1] : mat[i][j1] + mat[i][j2]);
                    ans = max(ans, val + temp);
                }
            }
            return dp[i][j1][j2] = (ans < 0 ? -1e9 : ans);
        };
        int res = solve(0, 0, n - 1);
        return max(0, res);
    }
};
