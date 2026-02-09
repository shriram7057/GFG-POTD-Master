class Solution {
  public:
    int maxProfit(vector<int>& arr) {
        int n = arr.size();
        if (n == 0) return 0;

        vector<int> buy(n, 0), sell(n, 0);

        // Base cases
        buy[0] = -arr[0]; // Buying on day 0
        sell[0] = 0;

        for (int i = 1; i < n; i++) {
            // Buy: either keep previous buy, or buy today after cooldown
            if (i >= 2)
                buy[i] = max(buy[i - 1], sell[i - 2] - arr[i]);
            else
                buy[i] = max(buy[i - 1], -arr[i]);

            // Sell: either keep previous sell, or sell today
            sell[i] = max(sell[i - 1], buy[i - 1] + arr[i]);
        }

        return sell[n - 1];
    }
};
