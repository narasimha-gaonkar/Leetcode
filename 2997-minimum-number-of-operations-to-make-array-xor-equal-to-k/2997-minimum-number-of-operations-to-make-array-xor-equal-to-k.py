class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        xorr = nums[0]
        
        for i in range(1, len(nums)):
            
            xorr ^= nums[i]
            
        res = xorr ^ k
        res = str(bin(res))
        return res.count('1')
            