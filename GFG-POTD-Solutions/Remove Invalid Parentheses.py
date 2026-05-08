from collections import deque

class Solution:
    def validParenthesis(self, s):
        
        def isValid(st):
            count = 0
            
            for ch in st:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    
                    if count < 0:
                        return False
            
            return count == 0
        
        res = []
        visited = set()
        q = deque([s])
        
        visited.add(s)
        found = False
        
        while q:
            curr = q.popleft()
            
            if isValid(curr):
                res.append(curr)
                found = True
            
            if found:
                continue
            
            for i in range(len(curr)):
                if curr[i] not in '()':
                    continue
                
                nxt = curr[:i] + curr[i+1:]
                
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        
        return sorted(list(set(res)))