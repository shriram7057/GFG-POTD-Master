class Solution:
    def countSubarrays(self, arr, k):
        # Code here
        from collections import defaultdict
        freq = defaultdict(int)
        freq[0] = 1
        odd_count = 0
        res = 0
        
        for x in arr:
            if x % 2 == 1:
               odd_count += 1
            res += freq[odd_count - k]
            freq[odd_count] += 1
        return res