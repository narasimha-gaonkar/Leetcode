class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        m = len(s)
        dp = [[-1] * 26 for _ in range(m)]
        
        def solve(i, c):
            if dp[i][c] != -1:
                return dp[i][c]
            dp[i][c] = 0
            
            match = c == (ord(s[i]) - ord('a'))
            
            if match: 
                dp[i][c] = 1
            if i > 0:
                dp[i][c] = solve(i-1, c)
                if match:
                    for p in range(26):
                        if abs(c - p) <= k:
                            dp[i][c] = max(dp[i][c], solve(i-1, p) + 1)
            return dp[i][c]
        res = 0
        for c in range(26):
            res = max(res, solve(m-1, c))
        return res
            
             
        
        
        