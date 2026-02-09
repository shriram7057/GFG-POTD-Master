class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        n = len(arr)
        window_sum=sum(arr[:k])
        max_sum = window_sum
        
        for i in range(k,n):
            window_sum += arr[i] - arr[i-k]
            if window_sum > max_sum:
                max_sum = window_sum
        return max_sum