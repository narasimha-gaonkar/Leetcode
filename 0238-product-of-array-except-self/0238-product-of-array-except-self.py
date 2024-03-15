class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        count_zero = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                count_zero += 1
        
        res = [0] * len(nums)
        # print(product, count_zero)
        for i in range(len(nums)):
            if nums[i] != 0 and count_zero == 0:
                res[i] = int(product / nums[i])
            elif nums[i] == 0 and count_zero == 1:
                res[i] = product
        # print(res)
        return res
        