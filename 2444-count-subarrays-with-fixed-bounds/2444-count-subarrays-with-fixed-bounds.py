class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        minn = maxx = split_point = -1
        res = 0
        
        for i in range(len(nums)):
            
            if nums[i] < minK or nums[i] > maxK:
                split_point = i
                
            if nums[i] == minK:
                minn = i
            
            if nums[i] == maxK:
                maxx = i
            
            res += max(0, min(minn, maxx) - split_point)
            
        return res