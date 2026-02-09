class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        from collections import defaultdict
        freq = defaultdict(int)
        left = 0
        res = 0
        distinct = 0
        
        for right in range(len(arr)):
            if freq[arr[right]] == 0:
                distinct += 1
            freq[arr[right]] += 1
            
            while distinct > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0 :
                    distinct -= 1
                left += 1
            res += right- left + 1
        return res
        