class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ''
        stack = []
        close_removal = []
        
        for i in range(len(s)):
            
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')' and stack:
                stack.pop()
            elif s[i] == ')':
                close_removal.append(i)
        # print(stack, close_removal)
        for i in range(len(s)):
            if i in stack or i in close_removal:
                continue
            res += s[i]
            
        return res
                
                