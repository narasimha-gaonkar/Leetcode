class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        nums_map = defaultdict(int)
        
        for i in nums:
            nums_map[i] +=1
        sums = 0
        
        
        for ele in nums_map:
            if nums_map[ele] == 1:
                sums += ele
        return sums
        