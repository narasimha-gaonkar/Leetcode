class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = j = 0
        while i < len(chars):
            count = 1
            
            while i < len(chars) - 1 and chars[i] == chars[i + 1]:
                count += 1
                i += 1
            
            chars[j] = chars[i]
            j += 1
            i += 1
            
            if count > 1:
                for k in str(count):
                    chars[j] = k
                    j +=1
        return j
            
            
                        
                    
                
            
            
            
                
                




        