class Solution:
    def maxProfit(self, x, y, a, b):
        tasks = []
        
        for i in range(len(a)):
            tasks.append((abs(a[i] - b[i]), a[i], b[i]))
        
        tasks.sort(reverse=True)
        
        profit = 0
        
        for _, pa, pb in tasks:
            
            if (pa >= pb and x > 0) or y == 0:
                profit += pa
                x -= 1
            else:
                profit += pb
                y -= 1
        
        return profit