import heapq
class Solution:
    def shortestPath(self, V, a, b, edges):
        # code here 
        a -= 1
        b -= 1
        INF=float('inf')
        adj=[[]for _ in range(V)]
        curved=[]
        for u,v,w_straight,w_curved in edges:
            u -= 1
            v -= 1
            adj[u].append((v,w_straight))
            adj[v].append((u,w_straight))
            curved.append((u,v,w_curved))
        def dijkstra(src):
            dist=[INF]*V
            dist[src]=0
            pq=[(0,src)]
            while pq:
                d,u=heapq.heappop(pq)
                if d>dist[u]:
                    continue
                for v,w in adj[u]:
                    if dist[v]>d+w:
                        dist[v]=d+w
                        heapq.heappush(pq,(dist[v],v))
            return dist
        distA = dijkstra(a)
        distB=dijkstra(b)
        ans=distA[b]
        
        for u ,v ,w in curved:
            if distA[u] != INF and distB[v] != INF:
                ans = min(ans, distA[u] + w + distB[v])
            if distA[v] != INF and distB[u] != INF:
                ans = min(ans,distA[v]+w+distB[u])
        return -1 if ans == INF else ans 
