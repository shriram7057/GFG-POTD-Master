class Solution:
    def findKRotation(self, arr):
        # code here
        n = len(arr)
        low,high= 0,n-1
        while low <= high:
            if arr[low] <= arr[high]:
                return low
            mid = (low+high) // 2
            prev = (mid - 1 + n) % n
            nxt = (mid + 1) % n
            if arr[mid] < arr[prev] and arr[mid] <= arr[nxt]:
                return mid
            elif arr[mid] >= arr[low]:
                low = mid + 1
            else:
                high = mid - 1
        return 0
        