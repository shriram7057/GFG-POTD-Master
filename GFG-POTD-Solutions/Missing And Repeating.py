class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        repeating = -1
        missing = -1
        
        for i in range(n):
            val = abs(arr[i])
            if arr[val - 1] < 0:
                repeating = val
            else:
                arr[val - 1] *= -1
        for i in range(n):
            if arr[i] > 0:
                missing = i+1
                break
        return [repeating, missing]
