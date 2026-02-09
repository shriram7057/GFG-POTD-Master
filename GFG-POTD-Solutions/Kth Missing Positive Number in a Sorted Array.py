class Solution:
    def kthMissing(self, arr, k):
        # code here
        n = len(arr)
        
        l,r=0,n-1
        
        while l <= r:
            mid = (l+r)// 2
            missing = arr[mid]-(mid+1)
            if missing < k:
                l = mid + 1
            else:
                r = mid - 1
        return l + k