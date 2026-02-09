class Solution:
    def countDistinct(self, arr, k):
        # Code here
        from collections import defaultdict
        freq= defaultdict(int)
        res = []
        
        for i in range(k):
            freq[arr[i]] += 1
        res.append(len(freq))
        
        for i in range(k,len(arr)):
            freq[arr[i-k]] -= 1
            if freq[arr[i-k]] == 0:
                del freq[arr[i-k]]
            freq[arr[i]] += 1
            res.append(len(freq))
        return res
        