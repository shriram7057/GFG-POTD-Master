class Solution:
    def minCost(self, costs : list[list[int]]) -> int:
        # code here
        n=len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        
        if k == 1:
            return -1 if n > 1 else costs[0][0]
        prev = costs[0][:]
        
        for i in range(1,n):
            min1 = min2 = float('inf')
            idx1 = -1
            for j in range(k):
                if prev[j] < min1:
                    min2 = min1
                    min1 = prev[j]
                    idx1 = j
                elif prev[j] < min2:
                    min2 = prev[j]
            curr = [0] * k
            for j in range(k):
                curr[j] = costs[i][j] + (min2 if j == idx1 else min1)
            prev = curr
        return min(prev)
                