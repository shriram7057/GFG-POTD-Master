class Solution:
    def sortIt(self, arr):
        # code here
        odds=[]
        evens=[]
        
        for x in arr:
            if x % 2 == 1:
                odds.append(x)
            else:
                evens.append(x)
        odds.sort(reverse=True)
        evens.sort()
        # return odds+evens
        arr[:] = odds + evens
    
