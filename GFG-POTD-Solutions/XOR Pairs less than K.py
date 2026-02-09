class TrieNode:
    def __init__(self):
        self.child=[None,None]
        self.cnt=0
class Solution:
    def cntPairs(self, arr, k):
        # code here
        def insert(root,num):
            node=root
            for i in range(31,-1,-1):
                bit=(num >> i) & 1
                if not node.child[bit]:
                    node.child[bit]=TrieNode()
                node=node.child[bit]
                node.cnt += 1
        def query(root,num,k):
            node=root
            count=0
            for i in range(31,-1,-1):
                if not node:
                    break
                bit_num=(num >> i) & 1
                bit_k = (k >> i) & 1
                
                if bit_k == 1:
                    if node.child[bit_num]:
                        count += node.child[bit_num].cnt
                    node=node.child[1-bit_num]
                else:
                    node=node.child[bit_num]
            return count
        root=TrieNode()
        ans=0
            
        for num in arr:
            ans += query(root,num,k)
            insert(root,num)
        return ans
                       