class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        presum = 0
        dp = {0 : 1}
        count = 0
        for num in nums:
            presum += num
            if presum - goal in dp:
                count += dp[presum - goal]
            
            dp[presum] = dp.get(presum, 0) + 1
        
        return count