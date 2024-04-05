class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        
        for letter in s:
            if stack and letter.lower() == stack[-1].lower() and ord(letter) != ord(stack[-1]):
                stack.pop()
            else:
                stack.append(letter)
                
        return ''.join(stack)