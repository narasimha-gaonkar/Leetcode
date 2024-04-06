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
        stack.extend(close_removal)       
        for i in range(len(s)):
            if i not in stack:
                res += s[i]
            
        return res
                
                