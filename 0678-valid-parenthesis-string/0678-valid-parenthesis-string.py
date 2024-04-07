class Solution:
    def checkValidString(self, s: str) -> bool:
        maxOpen, minOpen = 0, 0
        for i in s:
            if i == '(':
                maxOpen += 1
                minOpen += 1
            elif i == ')':
                maxOpen -= 1
                minOpen -= 1
            elif i == '*':
                maxOpen += 1
                minOpen -= 1
            
            if maxOpen < 0: return False
            if minOpen < 0: minOpen = 0

        if minOpen == 0: return True
        return False