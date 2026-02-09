class Solution:
    def maxRemove(self, stones):
        # Code here
        parent ={}
        rank={}
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
        for r,c in stones:
            row=("r",r)
            col=("c",c)
            if row not in parent:
                parent[row]=row
                rank[row]=0
            if col not in parent:
                parent[col]=col
                rank[col]=0
            union(row,col)
        comps=set()
        for x in parent:
            comps.add(find(x))
        return len(stones)-len(comps)