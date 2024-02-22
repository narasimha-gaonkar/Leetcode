class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        dp = {}
        
        def solve(target):
            if len(target) == 0:
                return 0
            if target in dp:
                return dp[target]
            
            cur_min = float('inf')
            
            for word in dictionary:
                if target.startswith(word):
                    cur_min  = min(solve(target[len(word):]), cur_min)

            cur_min = min(1 + solve(target[1:]), cur_min)
            dp[target] = cur_min
            return cur_min
        return solve(s)