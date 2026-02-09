class Solution:
	def firstNonRepeating(self, s):
		# code here
		from collections import deque,defaultdict
		freq = defaultdict(int)
		q = deque()
		res = []
		
		for ch in s:
		    freq[ch] += 1
		    q.append(ch)
		    
		    while q and freq[q[0]] > 1:
		        q.popleft()
		    if q:
		        res.append(q[0])
		    else:
		        res.append('#')
	    return ''.join(res)
		