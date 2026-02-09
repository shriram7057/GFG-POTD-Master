class TrieNode:
    def __init__(self):
        self.child={}
class Solution:
    def countSubs(self, s):
        # code here
        root=TrieNode()
        count=0
        
        for i in range(len(s)):
            curr=root
            for ch in s[i:]:
                if ch not in curr.child:
                    curr.child[ch]=TrieNode()
                    count+=1
                curr=curr.child[ch]
        return count