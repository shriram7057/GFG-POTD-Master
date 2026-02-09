class Solution:
    def transpose(self, mat):
        # code here
        n=len(mat)
        
        for i in range(n):
            for j in range(i+1 , n):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        return mat