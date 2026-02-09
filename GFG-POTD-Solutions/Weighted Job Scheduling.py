class Solution: 
    def maxProfit(self, jobs):
        # Sort jobs by end time
        jobs.sort(key=lambda x: x[1])
        n = len(jobs)
        dp = [0] * n
        dp[0] = jobs[0][2]
        
        # Binary search to find last non-conflicting job
        def findLastNonConflict(i):
            low, high = 0, i - 1
            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    if mid + 1 < i and jobs[mid + 1][1] <= jobs[i][0]:
                        low = mid + 1
                    else:
                        return mid
                else:
                    high = mid - 1
            return -1
        
        for i in range(1, n):
            incl_prof = jobs[i][2]
            l = findLastNonConflict(i)
            if l != -1:
                incl_prof += dp[l]
            dp[i] = max(incl_prof, dp[i - 1])
        
        return dp[-1]
