class Solution:
    def tsp(self, cost):
        n = len(cost)
        FULL = (1 << n) - 1
        
        from functools import lru_cache
        
        @lru_cache(None)   
        def solve(pos, mask):
            if mask == FULL:
                return cost[pos][0]
            
            ans = float('inf')
            for city in range(n):
                if not (mask & (1 << city)):
                    ans = min(ans, cost[pos][city] + solve(city, mask | (1 << city)))
            return ans
        
        return solve(0, 1)
