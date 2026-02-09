class Solution:
    def calculateSpan(self, arr):
        # code here
        stack = []
        n = len(arr)
        span=[0] * n
        
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            span[i]= i + 1 if not stack else i - stack[-1]
            stack.append(i)
        return span