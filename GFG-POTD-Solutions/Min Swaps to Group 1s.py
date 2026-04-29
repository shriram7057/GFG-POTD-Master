class Solution:
    def minSwaps(self, arr):
        ones = sum(arr)
        
        if ones == 0:
            return -1
        
        # count zeros in first window of size = ones
        zeros = ones - sum(arr[:ones])
        min_swaps = zeros
        
        for i in range(ones, len(arr)):
            if arr[i - ones] == 0:
                zeros -= 1
            if arr[i] == 0:
                zeros += 1
            
            min_swaps = min(min_swaps, zeros)
        
        return min_swaps