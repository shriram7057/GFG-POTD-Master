'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
class Solution:
    def flatten(self, root):
        # code here
        if not root or not root.next:
            return root
        def merge(a,b):
            dummy = Node(0)
            cur = dummy
            while a and b:
                if a.data <= b.data:
                    cur.bottom = a
                    a = a.bottom
                else:
                    cur.bottom = b
                    b = b.bottom
                cur = cur.bottom
            cur.bottom = a if a else b
            return dummy.bottom
        root.next = self.flatten(root.next)
        root = merge(root,root.next)
        root.next=None
        return root