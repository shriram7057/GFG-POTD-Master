class Solution:
    def subsetXOR(self, n : int):
        # code here
        def xor_to(n):
            if n%4==0:
                return n
            if n%4 == 1:
                return 1
            if n%4==2:
                return n+1
            return 0
        total=xor_to(n)
        if total==n:
            return list(range(1,n+1))
        need=total^n
        
        if need==0:
            return [n]
            
        ans=[]
        for i in range(1,n+1):
            if i != need:
                ans.append(i)
        return ans
        
