class Solution {
public:
    int minJumps(vector<int>& arr) {
        int n = arr.size();
        
        if (n == 1) return 0;

        unordered_map<int, vector<int>> mp;

        // Store indices for each value
        for (int i = 0; i < n; i++) {
            mp[arr[i]].push_back(i);
        }

        queue<int> q;
        vector<bool> vis(n, false);

        q.push(0);
        vis[0] = true;

        int steps = 0;

        while (!q.empty()) {
            int sz = q.size();

            while (sz--) {
                int i = q.front();
                q.pop();

                // Reached last index
                if (i == n - 1)
                    return steps;

                // i + 1
                if (i + 1 < n && !vis[i + 1]) {
                    vis[i + 1] = true;
                    q.push(i + 1);
                }

                // i - 1
                if (i - 1 >= 0 && !vis[i - 1]) {
                    vis[i - 1] = true;
                    q.push(i - 1);
                }

                // Same value jumps
                for (int idx : mp[arr[i]]) {
                    if (!vis[idx]) {
                        vis[idx] = true;
                        q.push(idx);
                    }
                }

                // Important optimization
                mp[arr[i]].clear();
            }

            steps++;
        }

        return -1;
    }
};