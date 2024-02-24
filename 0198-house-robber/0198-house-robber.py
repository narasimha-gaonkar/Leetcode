class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [-1] * len(nums)
        
        def solve(ind):
            
            if ind == 0:
                return nums[ind]
            if ind < 0:
                return 0
            if dp[ind] != -1:
                return dp[ind]

            take = nums[ind] + solve(ind-2)
            
            not_take = solve(ind-1)
            dp[ind] = max(take, not_take)
            return max(take, not_take)
        
        return solve(len(nums)-1)
            
            
            
        