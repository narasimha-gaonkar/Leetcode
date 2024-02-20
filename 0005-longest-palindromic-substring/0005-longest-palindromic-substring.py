class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = [[0] * len(s) for _ in range(len(s))]
        
        longestPalindrome = ''
        
        for i in range(len(s)):
            dp[i][i] = True
            longestPalindrome = s[i]
            
        for i in range(len(s)-1, -1, -1):
            
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    
                    if j-i == 1 or dp[i+1][j-1] == True:
                        dp[i][j] = True
                        if len(longestPalindrome) < len(s[i:j+1]):
                            longestPalindrome = s[i:j+1]
                            
        return longestPalindrome
                        
        
        
        
        
                
#         if len(s) == 1:
#             return s
        
#         maxcount = 0
#         palstring = ''
        
#         for idx in range(len(s)):
#             l , r = idx, idx
#             count = 1
#             while l > 0 and r < len(s)-1:

#                 if s[l-1] == s[r+1]:
#                     count+=2
#                 else:
#                     break
#                 l-=1
#                 r+=1
#             if count > maxcount:

#                 maxcount = count
#                 palstring = s[l:r+1]
        
        
#         for idx in range(len(s)-1):
#             l , r = idx, idx+1
#             count = 0
#             if s[l] == s[r]:
#                 count+=2
#             else:
#                 continue
#             while l > 0 and r < len(s)-1:

#                 if s[l-1] == s[r+1]:
#                     count+=2
#                 else:
#                     break
#                 l-=1
#                 r+=1
#             if count > maxcount:

#                 maxcount = count
#                 palstring = s[l:r+1]
        
#         return palstring