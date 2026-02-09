class Solution:
	def andInRange(self, l, r):
		# code here
		shift =0
		while l < r:
		    l>>=1
		    r>>=1
		    shift += 1
		return l << shift
