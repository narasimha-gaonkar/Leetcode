class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        end = len(s) - 1
        res = 0
        
        while s[end] == ' ':
            end -= 1
            
        while s[end] != ' ' and end >= 0:
            res += 1
            end -= 1
        return res
        