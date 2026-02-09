class Solution:
    def minCostPath(self, mat):
        # code here
        n,m=len(mat),len(mat[0])
        effort=[[float('inf')]* m for _ in range(n)]
        effort[0][0]=0
        pq=[(0,0,0)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        
        while pq:
            curr_eff,r,c=heapq.heappop(pq)
            
            if r == n-1 and c == m-1:
                return curr_eff
            if curr_eff>effort[r][c]:
                continue
            for dr , dc in directions:
                nr, nc = r+dr,c+dc 
                if 0 <= nr < n and 0<= nc <m:
                    new_eff=max(curr_eff,abs(mat[r][c]-mat[nr][nc]))
                    if new_eff<effort[nr][nc]:
                        effort[nr][nc]=new_eff
                        heapq.heappush(pq,(new_eff,nr,nc))
        return effort[n-1][m-1]