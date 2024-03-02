class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        res = [None] * len(nums)
        
        l = 0
        r = len(nums) - 1
        p = len(nums) - 1
        
        while l<=r:
            # print(l,r , nums[l], nums[r], res)    
            if abs(nums[l]) > abs(nums[r]):
                res[p] = nums[l] * nums[l]
                p -= 1
                l+=1
                
            elif abs(nums[l]) < abs(nums[r]):
                res[p] = nums[r] * nums[r]
                p -= 1
                r-=1
            else:
                res[p] = nums[r] * nums[r]
                p -= 1
                r-=1
        return res
        
                
        