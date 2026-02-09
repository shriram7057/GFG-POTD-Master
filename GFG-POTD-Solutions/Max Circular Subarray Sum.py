class Solution:
    def maxCircularSum(self, arr):
        # code here
        def kadane(a):
            max_ending=max_so_far = a[0]
            for x in a[1:]:
                max_ending = max(x,max_ending + x)
                max_so_far = max(max_so_far,max_ending)
            return max_so_far
        max_kadane = kadane(arr)
        
        total_sum = sum(arr)
        min_kadane = kadane([-x for x in arr])
        max_wrap = total_sum + min_kadane
        
        if max_wrap == 0:
            return max_kadane
        return max(max_kadane,max_wrap)