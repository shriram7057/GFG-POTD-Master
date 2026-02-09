class Solution {
    public int numberOfPath(int[][] mat, int k) {
        int m = mat.length;
        int n = mat[0].length;

        // dp[i][j][c] = number of paths to cell (i,j) with coin sum c
        int[][][] dp = new int[m][n][k + 1];

        // Initialize starting cell
        if (mat[0][0] <= k) {
            dp[0][0][mat[0][0]] = 1;
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int c = 0; c <= k; c++) {
                    if (dp[i][j][c] > 0) {
                        // Move down
                        if (i + 1 < m && c + mat[i + 1][j] <= k) {
                            dp[i + 1][j][c + mat[i + 1][j]] += dp[i][j][c];
                        }
                        // Move right
                        if (j + 1 < n && c + mat[i][j + 1] <= k) {
                            dp[i][j + 1][c + mat[i][j + 1]] += dp[i][j][c];
                        }
                    }
                }
            }
        }

        return dp[m - 1][n - 1][k];
    }
}
