class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = -1
        
        occ = 0
        
        for num in nums:
            
            if occ == 0:
                ele = num
                occ = 1
            elif num == ele:
                occ += 1
            else:
                occ -= 1
                
        occ = 0
        for num in nums:
            if num == ele:
                occ += 1
        if occ > len(nums) / 2:
            return ele
        return -1