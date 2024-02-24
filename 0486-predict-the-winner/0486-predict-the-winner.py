class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = [[-1] * len(nums) for _ in range(len(nums))]
        
        def solve(i,j):
            # invalid state
            if i > j:
                return 0
            
            if i == j:
                return nums[i]
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            score_diff_i = nums[i] - solve(i+1,j) 
            score_diff_j = nums[j] - solve(i,j-1)
            
            dp[i][j] = max(score_diff_i,score_diff_j)
            return max(score_diff_i,score_diff_j)
        
        return solve(0,len(nums)-1) >= 0
