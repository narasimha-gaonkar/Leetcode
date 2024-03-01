class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        res = ['0'] * len(s)
        
        n = s.count('1')
        
        res[-1] = '1'
        
        if n == 1: return ''.join(res)
        
        for i in range(n-1):
            res[i] = '1'
        
        return ''.join(res)