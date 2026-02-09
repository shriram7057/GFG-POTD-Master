class Solution:
    def maxOnes(self, arr, k):
        # code here
        left = 0
        zeros = 0
        ans = 0
        
        for right in range(len(arr)):
            if arr[right] == 0:
                zeros += 1
            while zeros > k:
                if arr[left] == 0:
                    zeros -= 1
                left += 1
            ans = max(ans,right - left + 1)
        return ans