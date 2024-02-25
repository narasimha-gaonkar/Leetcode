class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # Brute force gice O(n3)
        if len(nums) == 1: return nums[0]
        maximum_num = float(-inf)
        prefix = 1
        suffix = 1
        
        
        n = len(nums)
        
        for i in range(n):
            
            if prefix == 0: prefix = 1
            prefix = prefix * nums[i]
            
            if suffix == 0: suffix = 1
            suffix = suffix * nums[n - i -1]
            
            maximum_num = max(maximum_num, prefix, suffix)
                
                
        return maximum_num
            
            
        
        
        