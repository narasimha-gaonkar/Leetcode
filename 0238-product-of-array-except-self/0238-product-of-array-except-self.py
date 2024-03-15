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


#         for num in nums:
#             if num != 0:
#                 product *= num
#             else:
#                 count_zero += 1
        
#         res = [0] * len(nums)

#         for i in range(len(nums)):
#             if nums[i] != 0 and count_zero == 0:
#                 res[i] = int(product / nums[i])
#             elif nums[i] == 0 and count_zero == 1:
#                 res[i] = product
#         return res
        