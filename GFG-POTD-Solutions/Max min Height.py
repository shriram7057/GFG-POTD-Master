class Solution():
    def maxMinHeight(self, arr, k, w):
        # code here
        n = len(arr)
        def can_make(target):
            temp = [0] * (n+1)
            curr_add = 0
            days_used = 0
            
            for i in range(n):
                curr_add += temp[i]
                current_height = arr[i] + curr_add
                
                if current_height < target:
                    need = target - current_height
                    days_used += need
                    
                    if days_used > k:
                        return False
                    curr_add += need
                    if i + w < n:
                        temp[i+w] -= need
            return True
        low = min(arr)
        high = low + k
        ans = low
        
        while low <= high:
            mid = (low+high) //2
            if can_make(mid):
                ans = mid
                low = mid+1
            else:
                high = mid - 1
        return ans 