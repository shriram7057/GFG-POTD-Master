class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []

        for i in range(n):
            if arr[i] != -1:
                l = max(0, i - arr[i])
                r = min(n - 1, i + arr[i])
                intervals.append((l, r))

        intervals.sort()

        res = 0
        i = 0
        curr_end = 0
        farthest = 0

        while curr_end < n:
            while i < len(intervals) and intervals[i][0] <= curr_end:
                farthest = max(farthest, intervals[i][1] + 1)
                i += 1

            if farthest == curr_end:
                return -1

            res += 1
            curr_end = farthest

        return res
