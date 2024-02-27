class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        enc = {}
        count = 1
        
        for letter in key:
            if letter.isalpha() and letter not in enc:
                enc[letter] = count
                count+=1
                
        res = ''
        
        for letter in message:
            if letter.isalpha():
                res = res + chr(enc[letter] + 96)
            elif letter == ' ':
                res = res + ' '
        return res
        