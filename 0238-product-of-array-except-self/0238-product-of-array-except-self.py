class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product_pre = product_post =  1
        n = len(nums)
        res = [1] * n
        postfix_sum = [1] * n
        prefix_sum = [1] * n

        
        for i in range(n):
            prefix_sum[i] = product_pre
            product_pre *= nums[i]
            
            postfix_sum[n - i - 1] = product_post
            product_post *= nums[n - i - 1]
            
        for i in range(n):
            res[i] = postfix_sum[i] * prefix_sum[i]
            
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
        