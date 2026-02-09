class Solution:
    def minConnect(self, V, edges):
        # code here
        parent=list(range(V))
        rank=[0]*V
        if len(edges)<V-1:
            return -1
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(a,b):
            ra,rb=find(a),find(b)
            if ra!=rb:
                if rank[ra]<rank[rb]:
                    parent[ra]=rb
                elif rank[ra]>rank[rb]:
                    parent[rb]=ra
                else:
                    parent[rb]=ra
                    rank[ra]+=1
        for u , v in edges:
            union(u,v)
        comp=len({find(i) for i in range(V)})
        return comp -1