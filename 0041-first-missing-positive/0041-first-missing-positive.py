class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        i = 0
        
        for i in range(n):
            actual_pos = nums[i] - 1
            
            while nums[i] > 0 and nums[i] <= n and nums[i] != nums[actual_pos]:
                nums[i], nums[actual_pos] = nums[actual_pos], nums[i]
                actual_pos = nums[i] - 1 
        # print(nums)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return len(nums) + 1
        