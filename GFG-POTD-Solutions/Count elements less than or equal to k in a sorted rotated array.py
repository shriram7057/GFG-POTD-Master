class Solution:
    def countLessEqual(self, arr, x):
        #code here
        n = len(arr)
        if n == 0:
            return 0
        l , r = 0,n-1
        while l<r:
            mid = (l+r) // 2
            if arr[mid] > arr[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l
        
        def upper_bound(lo,hi):
            ans = -1
            while lo <= hi:
                mid=(lo+hi) // 2
                if arr[mid] <= x:
                    ans = mid 
                    lo = mid + 1
                else:
                    hi = mid -1
            return ans
        if x < arr[pivot]:
            return 0
        if pivot == 0:
            idx = upper_bound(0,n-1)
            return idx +1 if idx != -1 else 0
        if x <= arr[n-1]:
            idx = upper_bound(pivot,n-1)
            return idx - pivot + 1 if idx != -1 else 0
        else:
            idx1= upper_bound(pivot,n-1)
            idx2= upper_bound(0,pivot-1)
            count = 0
            if idx1 != -1:
                count += idx1 - pivot +1
            if idx2 != -1:
                count += idx2 + 1
            return count        