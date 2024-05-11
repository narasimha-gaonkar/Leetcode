class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_product = 1
        post_product = 1
        res = [0] * n
        cur_product = 1
        for i in range(n):
            res[i] = cur_product
            cur_product *= nums[i]
        cur_product = 1    
        for i in range(n-1, -1, -1):
            res[i] *= cur_product
            cur_product *= nums[i]
            
            # res[i] = post_product[i] * pre_product[i]
        
        return res
        
        