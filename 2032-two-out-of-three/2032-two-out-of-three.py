class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        one_two = set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3)
        
        print(one_two)
        return one_two
        