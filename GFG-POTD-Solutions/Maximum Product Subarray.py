class Solution:
	def maxProduct(self,arr):
		# code here
		max_ending = arr[0]
		min_ending = arr[0]
		ans = arr[0]
		
		for i in range(1,len(arr)):
		    x = arr[i]
		    
		  #  max_ending,min_ending = min_ending,max_ending
		    temp_max = max(x,max_ending * x,min_ending * x)
		    temp_min = min(x,max_ending * x,min_ending * x)
		    max_ending = temp_max
		    min_ending = temp_min
		    
		    ans = max(ans,max_ending)
		    
		return  ans