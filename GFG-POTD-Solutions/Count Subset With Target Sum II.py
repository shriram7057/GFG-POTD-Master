class Solution:
    def countSubset(self, arr, k):
        from collections import Counter

        n = len(arr)
        mid = n // 2

        left = arr[:mid]
        right = arr[mid:]

        left_sums = []
        for mask in range(1 << len(left)):
            s = 0
            for i in range(len(left)):
                if mask & (1 << i):
                    s += left[i]
            left_sums.append(s)

        right_count = Counter()
        for mask in range(1 << len(right)):
            s = 0
            for i in range(len(right)):
                if mask & (1 << i):
                    s += right[i]
            right_count[s] += 1

        ans = 0
        for s in left_sums:
            ans += right_count[k - s]

        return ans
