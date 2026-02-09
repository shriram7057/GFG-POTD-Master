class Solution:
    def findPeakGrid(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])
        
        l, r = 0, m-1
        while l <= r:
            mid = (l+r)//2
            max_row = 0
            for i in range(n):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
                    
            left = mat[max_row][mid - 1] if mid - 1 >= 0 else float('-inf')
            right = mat[max_row][mid+1] if mid + 1 < m else float('-inf')
            if mat[max_row][mid] >= left and mat[max_row][mid] >= right:
                return [max_row,mid]
            elif mat[max_row][mid] < right:
                l = mid + 1
            else:
                r = mid - 1
        return [-1,-1]