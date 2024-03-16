class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        length = 0
        
        count = 0
        
        hmap = {0 : -1}
        
        for idx, num in enumerate(nums):
            
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in hmap:
                length = idx - hmap[count]
                
                max_length = max(length, max_length)
            else:
                hmap[count] = idx
        
        return max_length
