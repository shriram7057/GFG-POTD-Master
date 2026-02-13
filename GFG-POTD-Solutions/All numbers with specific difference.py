class Solution:
    def getCount(self, n, d):
        # code here 
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        low,high= 1, n
        first_valid = n + 1
        
        while low <= high:
            mid =(low+high) // 2
            if mid - digit_sum(mid) >= d:
                first_valid = mid
                high = mid - 1
            else:
                low = mid + 1
        
        if first_valid == n + 1:
            return 0
        return n - first_valid + 1
        