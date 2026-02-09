class Solution:
    def swapDiagonal(self, mat):
      # code here
      
      n=len(mat)
      
      for i in range(n):
        j=n - 1 - i
        mat[i][i], mat[i][j] = mat[i][j], mat[i][i]
      return mat