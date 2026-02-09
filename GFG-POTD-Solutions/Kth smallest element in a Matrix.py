class Solution:
    def kthSmallest(self, mat, k):
        # code here
        n = len(mat)
        low,high = mat[0][0],mat[n-1][n-1]
        
        def countLessEquals(x):
            cnt = 0
            j=n-1
            for i in range(n):
                while j >= 0 and mat[i][j]> x:
                    j -= 1
                cnt += (j+1)
            return cnt
        while low < high:
            mid = (low+high)//2
            if countLessEquals(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low