class Solution:
    def isSubTree(self, root1, root2):
        
        def isSame(a, b):
            if not a and not b:
                return True
            
            if not a or not b:
                return False
            
            return (a.data == b.data and
                    isSame(a.left, b.left) and
                    isSame(a.right, b.right))
        
        if root2 is None:
            return True
        
        if root1 is None:
            return False
        
        if isSame(root1, root2):
            return True
        
        return (self.isSubTree(root1.left, root2) or
                self.isSubTree(root1.right, root2))