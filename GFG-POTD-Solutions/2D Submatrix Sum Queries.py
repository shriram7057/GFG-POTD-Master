class Solution:
    def prefixSum2D(self, mat, queries):
        # code here 
        n=len(mat)
        m=len(mat[0])
        
        pref=[[0] * (m+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                pref[i][j] = (
                    mat[i-1][j-1]
                    + pref[i-1][j]
                    + pref[i][j-1]
                    - pref[i-1][j-1]
                )
        res = []
        for r1,c1,r2,c2 in queries:
            r1 += 1
            c1 += 1
            r2 += 1
            c2 += 1
            sub_sum=(
                pref[r2][c2]
                - pref[r1-1][c2]
                - pref[r2][c1-1]
                + pref[r1-1][c1-1]
            )
            res.append(sub_sum)
        return res
        