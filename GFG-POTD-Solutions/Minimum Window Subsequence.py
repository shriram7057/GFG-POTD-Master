class Solution:
    def minWindow(self, s1, s2):
        # Code here
        n,m=len(s1),len(s2)
        min_len= float('inf')
        start = -1
        
        i = 0
        while i < n:
            if s1[i] == s2[0]:
                j = 0
                k = i
                while k < n and j < m:
                    if s1[k] == s2[j]:
                        j += 1
                    k += 1
                if j == m:
                    end = k - 1
                    j -= 1
                    while j >= 0:
                        if s1[end] == s2[j]:
                            j -= 1
                            
                        end -= 1
                    end += 1
                    
                    if k - end < min_len:
                        min_len = k - end
                        start= end
                        
                    i = end + 1
                    continue
            i += 1
        return "" if start == -1 else s1[start:start + min_len] 
        