class Solution {
  public:
    int maxPeople(vector<int> &arr) {
        // code here
        int n = arr.size();
        vector<int> leftBlock(n,-1),rightBlock(n,n);
        stack<int> st;
        
        for (int i = 0;i<n;i++)
        {
            while(!st.empty() && arr[st.top()] < arr[i])
            {
                st.pop();
            }
            if (!st.empty())
            {
                leftBlock[i] = st.top();
            }
            st.push(i);
        }
        while (!st.empty()) st.pop();
        for(int i = n - 1;i >= 0; i-- )
        {
            while(!st.empty() && arr[st.top()] < arr[i])
            {
                st.pop();
            }
            if (!st.empty())
            {
                rightBlock[i] = st.top();
            }
            st.push(i);
        }
        int ans = 0;
        for(int i = 0;i<n;i++)
        {
            int visible = (i-leftBlock[i] - 1) + (rightBlock[i] - i - 1) + 1;
            ans = max(ans,visible);
        }
        return ans;
    }
};