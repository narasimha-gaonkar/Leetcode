class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        nums_map = defaultdict(int)
        sums = 0
        for i in nums:
            nums_map[i] +=1
            if nums_map[i]  == 2:
                sums -= i
            elif nums_map[i] == 1:
                sums += i
        return max(sums, 0)
#         sums = 0
        
#         for ele in nums_map:
#             if nums_map[ele] == 1:
#                 sums += ele
#         return sums
        