class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        max_ele = max(nums)
        
        count = start = max_ele_window = 0
        
        for end in range(len(nums)):
            
            if nums[end] == max_ele:
                max_ele_window += 1
            while max_ele_window == k:
                if nums[start] == max_ele:
                    max_ele_window -= 1
                start += 1
            count += start
        return count 