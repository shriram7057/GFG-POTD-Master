class Solution:
    def minCost(self, heights, cost):
        # code here
        def total_cost(target):
            total = 0
            for h,c in zip(heights,cost):
                total += abs(h-target) * c
            return total
        low,high = min(heights),max(heights)
        ans = float('inf')
        
        while low <= high:
            mid =(low+high) // 2
            cost1 = total_cost(mid)
            cost2 = total_cost(mid + 1)
            
            ans = min(cost1,cost2)
            
            if cost1 < cost2:
                high = mid - 1
            else:
                low = mid + 1
        return ans