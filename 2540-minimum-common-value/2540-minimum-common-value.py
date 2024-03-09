class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        dict_nums = defaultdict(int)
        
        for i in nums1:
            dict_nums[i] = 1
        
        for j in nums2:
            if j in dict_nums:
                return j
        return -1