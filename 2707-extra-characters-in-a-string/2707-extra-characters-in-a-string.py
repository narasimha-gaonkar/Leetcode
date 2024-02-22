class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        dp = [float('inf')] * (len(s) + 1)
        dp[0] = 0
        
        for i in range(1, len(s) + 1):
            for word in dictionary:
                if i >= len(word) and s[i - len(word):i] == word:
                    dp[i] = min(dp[i], dp[i - len(word)])
            
            dp[i] = min(dp[i], dp[i - 1] + 1)
                
                
        return dp[len(s)]
    
#         def solve(target):
#             if len(target) == 0:
#                 return 0
#             if target in dp:
#                 return dp[target]
            
#             cur_min = float('inf')
            
#             for word in dictionary:
#                 if target.startswith(word):
#                     cur_min  = min(solve(target[len(word):]), cur_min)

#             cur_min = min(1 + solve(target[1:]), cur_min)
#             dp[target] = cur_min
#             return cur_min
#         return solve(s)