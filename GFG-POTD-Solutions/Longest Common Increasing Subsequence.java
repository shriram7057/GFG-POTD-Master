class Solution {
    public int LCIS(int[] a, int[] b) {
        // code here
        int n=a.length,m=b.length;
        int[] dp=new int[m];
        int result = 0;
        for(int i=0;i<n;i++)
        {
            int current =0; 
            for(int j=0;j<m;j++)
            {
                if(a[i]==b[j])
                {
                    dp[j]=Math.max(dp[j],current+1);
                    result=Math.max(result,dp[j]);
                }else if (a[i]>b[j])
                {
                    current=Math.max(current,dp[j]);
                }
            }
            // return result;
        }
        return result;
    }
}