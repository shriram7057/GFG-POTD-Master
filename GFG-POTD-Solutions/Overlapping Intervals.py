class Solution:
	def mergeOverlap(self, arr):
		# Code here
		if not arr:
		    return []
		arr.sort(key=lambda x: x[0])
		res=[arr[0]]
		
		for i in range(1,len(arr)):
		    last=res[-1]
		    curr=arr[i]
		    
		    if curr[0] <= last[1]:
		        last[1]=max(last[1],curr[1])
		    else:
		        res.append(curr)
		return res