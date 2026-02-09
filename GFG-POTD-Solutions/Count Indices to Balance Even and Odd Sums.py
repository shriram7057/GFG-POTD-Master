class Solution:
    def cntWays(self, arr):
        # code here
        n=len(arr)
        even_sum=0
        odd_sum=0
        
        for i in range(n):
            if i%2 == 0:
                even_sum += arr[i]
            else:
                odd_sum += arr[i]
        left_even=0
        left_odd=0
        count=0
        for i in range(n):
            if i % 2 == 0:
                even_sum -= arr[i]
            else:
                odd_sum -= arr[i]
            if left_even + odd_sum == left_odd + even_sum:
                count += 1
            if i % 2 == 0:
                left_even += arr[i]
            else:
                left_odd += arr[i]
        return count