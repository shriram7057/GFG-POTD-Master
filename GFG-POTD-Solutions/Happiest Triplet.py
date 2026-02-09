class Solution:
    def smallestDiff(self,a, b, c):
        #code here.
        a.sort()
        b.sort()
        c.sort()
        i=j=k=0
        
        n,m,p=len(a),len(b),len(c)
        
        best_diff = float('inf')
        best_sum = float('inf')
        
        best_triplet = None
        
        while i < n and j < m and k < p:
            x,y,z=a[i],b[j],c[k]
            cur_max = max(x,y,z)
            cur_min = min(x,y,z)
            diff = cur_max - cur_min
            s = x + y +z
            
            if diff < best_diff or (diff==best_diff and s< best_sum):
                best_diff=diff
                best_sum = s
                best_triplet=[x,y,z]
                
            if cur_min == x:
                i += 1
            elif cur_min == y:
                j += 1
            else:
                k += 1
        best_triplet.sort(reverse=True)
        return best_triplet