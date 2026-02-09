class Solution:
    def cntInRange(self, arr, queries):
        # code here
        import bisect
        arr.sort()
        res=[]      
        for a,b in queries:
            left = bisect.bisect_left(arr,a)
            right = bisect.bisect_right(arr,b)
            res.append(right - left)
        return res