class Solution:
    def subarrayRanges(self, arr):
        # Code here
        n = len(arr)
        def sumSubarrayMax():
            stack=[]
            res = 0
            for i in range(n+1):
                while stack and (i==n or arr[stack[-1]] < arr[i]):
                    mid = stack.pop()
                    left = mid - stack[-1]if stack else mid + 1
                    rigth = i - mid 
                    res += arr[mid] * left * rigth
                stack.append(i)
            return res
        def sumSubarrayMin():
            stack = []
            res = 0
            for i in range(n+1):
                while stack and (i == n or arr[stack[-1]] > arr[i]):
                    mid = stack.pop()
                    left = mid - stack[-1] if stack else mid + 1
                    right = i - mid 
                    res += arr[mid] * left * right
                stack.append(i)
            return res
        return sumSubarrayMax()-sumSubarrayMin()