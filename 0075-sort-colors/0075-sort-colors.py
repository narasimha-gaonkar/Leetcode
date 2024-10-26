class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k, i, j = 0, 0, len(nums) - 1
        
        while i <= j:
            
            if nums[i] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        