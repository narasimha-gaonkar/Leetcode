class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        summ = sum(nums)
        
        left_sum = 0
        prev = 0

        for idx, num in enumerate(nums):
            summ -= num
            left_sum += prev
            
            if summ == left_sum:
                return idx
            prev = num
        return -1