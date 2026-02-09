class Solution:
    def searchInsertK(self, arr, k):
        # code here
        low , high = 0, len(arr) - 1
        while low <= high:
            mid=(low+high) // 2
            
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid -1 
        return low