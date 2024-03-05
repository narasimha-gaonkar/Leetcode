class Solution:
    def minimumLength(self, s: str) -> int:
        
        i = 0 
        j = len(s) - 1
        
        while i < j:
            print(i,j, s[i], s[j])
            
            if s[i] == s[j]:
                if j - i == 1:
                    return 0
                
                while i<j:
                    if s[i] == s[i+1]:
                        i += 1
                    else:
                        break
                while i<j:
                    if s[j] == s[j - 1]:
                        j -= 1
                    else:
                        break
                i += 1
                j -= 1
                if i > j:
                    return 0
            else:
                return j - i + 1
                
        return 1
            
        