class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        dp = [[0] * 2 for _ in range(n)]
        no_team = 0
        for i in range(n):
            for j in range(i):
                
                if rating[j] < rating[i]:
                    no_team += dp[j][0]
                    dp[i][0] += 1
                elif rating[j] > rating[i]:
                    no_team += dp[j][1]
                    dp[i][1] += 1
        return no_team