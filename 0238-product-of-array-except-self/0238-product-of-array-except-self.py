class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product_pre = product_post =  1
        n = len(nums)
        res = [1] * n
        
        for i in range(n):
            res[i] = product_pre
            product_pre *= nums[i]
                        
        for i in range(n-1, -1, -1):
            res[i] = res[i] * product_post
            product_post *= nums[i]
        return res
        