class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append('*')
        prev = chars[0]
        left = 0
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == prev:
                count += 1
            else:
                chars[left] = prev
                left += 1
                if count > 1:  # Compression needed
                    if count < 10:
                        chars[left] = str(count)
                        left += 1
                    else:
                        # Handling counts >= 10
                        for k in str(count):
                            chars[left] = k
                            left += 1
                count = 1
            prev = chars[i]
        return left
                        
                    
                
            
            
            
                
                




        