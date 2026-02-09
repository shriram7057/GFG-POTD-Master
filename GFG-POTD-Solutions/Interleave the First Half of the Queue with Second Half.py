class Solution:
    def rearrangeQueue(self, q):
        #code here 
        from collections import deque
        n = len(q)
        half = n // 2
        dq = deque(q)
        first = deque()
        
        for _ in range(half):
            first.append(dq.popleft())
        res = deque()
        while first:
            res.append(first.popleft())
            res.append(dq.popleft())
        q.clear()
        q.extend(res)