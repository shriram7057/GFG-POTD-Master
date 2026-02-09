Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def minCost(self, s, t, transform, cost):
...         # code here
...         n=len(s)
...         INF=float('inf')
...         ALPHABET=26
...         
...         dist=[[INF]* ALPHABET for _ in range(ALPHABET)]
...         for i in range(ALPHABET):
...             dist[i][i]=0
...         
...         for (u,v), c in zip(transform,cost):
...             u_idx=ord(u)-ord('a')
...             v_idx=ord(v)-ord('a')
...             dist[u_idx][v_idx]=min(dist[u_idx][v_idx],c)
...             
...         for k in range(ALPHABET):
...             for i in range(ALPHABET):
...                 for j in range(ALPHABET):
...                     if dist[i][k]+dist[k][j]<dist[i][j]:
...                         dist[i][j]=dist[i][k]+dist[k][j]
...         total_cost=0
...         for i in range(n):
...             u=ord(s[i])-ord('a')
...             v=ord(t[i])-ord('a')
...             best=INF
...             for x in range(ALPHABET):
...                 if dist[u][x] != INF and dist[v][x] != INF:
...                     best=min(best,dist[u][x]+dist[v][x])
...             if best == INF:
...                 return -1
...             total_cost+=best
