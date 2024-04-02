class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        freq = {}
        
        for i in range(len(s)):
            
            if s[i] in freq and freq[s[i]] != t[i]:
                return False
            elif s[i] not in freq:
                if t[i] in freq.values():
                        return False
                freq[s[i]] = t[i]
                
        return True