class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        dict = {}
        
        for i in nums1:
            dict[i] = i
        
        res = set()
        
        for i in nums2:
            if i in dict:
                res.add(i)
        return res