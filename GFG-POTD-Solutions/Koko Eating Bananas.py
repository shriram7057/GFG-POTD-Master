class Solution:
    def kokoEat(self, arr, k):
        # Code here
        def hours_needed(s):
            total = 0
            for x in arr:
                total += (x + s - 1) // s
            return total
        
        low,high = 1,max(arr)
        ans = high
        
        while low <= high:
            mid =(low+high) // 2
            if hours_needed(mid)<= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        