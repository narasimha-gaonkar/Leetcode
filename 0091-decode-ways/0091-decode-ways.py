class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == '0':
            return 0
        n = len(s) + 1
        
        dp = [0] * (n)
        
        dp[0] = dp[1] = 1
        for i in range(2, n):
            
            #check if i can decode this letter:
            
            if 1 <= int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
                
            #check if we can form a letter using previos and current char
            # print(int(s[i-1]), int(s[i-2:i]))
            
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]
            