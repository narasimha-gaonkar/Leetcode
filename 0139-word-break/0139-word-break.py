class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = {}
        def solve(target):
            if len(target) == 0:
                return True
            if target in dp:
                return dp[target]
            for word in wordDict:
                if target[:len(word)] == word:
                    if solve(target[len(word):]):
                        dp[target] = True
                        return True
            dp[target] = False
            return False
        
        return solve(s)
        
        
                    