class Solution:
    def nextFreqGreater(self, arr):
        # code here
        from collections import Counter
        freq = Counter(arr)
        stack = []
        n = len(arr)
        res = [-1] * n
        
        for i in range(n):
            while stack and freq[arr[stack[-1]]] < freq[arr[i]]:
                res[stack.pop()] = arr[i]
            stack.append(i)
        return res