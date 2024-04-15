class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_product = [None]*n
        pre = 1
        for i in range(n):
            pre_product[i] = pre
            pre *= nums[i]
        pre = 1
        
        for i in range(n-1, -1, -1):
            pre_product[i] = pre * pre_product[i]
            pre *= nums[i]
        return pre_product
        
        
        