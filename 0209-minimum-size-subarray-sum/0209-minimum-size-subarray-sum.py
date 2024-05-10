class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = 0
        
        min_length = float(inf)
        l = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            while prefix_sum >= target:
                if prefix_sum >= target:
                    min_length = min(i - l + 1, min_length)
                prefix_sum -= nums[l]
                l += 1
                
        return 0 if min_length == float(inf) else  min_length
                
                