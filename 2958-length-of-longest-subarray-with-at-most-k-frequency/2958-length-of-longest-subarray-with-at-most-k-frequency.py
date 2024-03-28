class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        start = -1
        end = 0
        res = 0
        
        freq = {}
        
        for end in range(len(nums)):
            
            freq[nums[end]] = freq.get(nums[end], 0) + 1
            
            while freq[nums[end]] > k:
                start += 1
                freq[nums[start]] -= 1
            res = max(res, end - start)
        
        return res
            
        