class Solution:
    def longestPalindrome(self, s: str) -> str:
                
        if len(s) == 1:
            return s
        
        maxcount = 0
        palstring = ''
        
        for idx in range(len(s)):
            l , r = idx, idx
            count = 1
            while l > 0 and r < len(s)-1:

                if s[l-1] == s[r+1]:
                    count+=2
                else:
                    break
                l-=1
                r+=1
            if count > maxcount:

                maxcount = count
                palstring = s[l:r+1]
        
        
        for idx in range(len(s)-1):
            l , r = idx, idx+1
            count = 0
            if s[l] == s[r]:
                count+=2
            else:
                continue
            while l > 0 and r < len(s)-1:

                if s[l-1] == s[r+1]:
                    count+=2
                else:
                    break
                l-=1
                r+=1
            if count > maxcount:

                maxcount = count
                palstring = s[l:r+1]
        
        return palstring