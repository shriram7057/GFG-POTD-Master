class Solution():
    def checkRedundancy(self, s):
        # code here 
        stack = []
        for ch in s:
            if ch == ')':
                has_operator = False
                while stack and stack[-1] != '(':
                    if stack[-1] in '+-*/':
                        has_operator= True
                    stack.pop()
                stack.pop()
                if not has_operator:
                    return True
            else:
                stack.append(ch)
        return False