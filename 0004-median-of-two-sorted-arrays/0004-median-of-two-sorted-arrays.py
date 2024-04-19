class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
     
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        
        def get_min():
            nonlocal i, j
            if i < m and j < n:
                if nums1[i] <= nums2[j]:
                    ans = nums1[i]
                    i += 1
                else:
                    ans = nums2[j]
                    j += 1
            elif j == n:
                ans = nums1[i]
                i += 1
            else:
                ans = nums2[j]
                j += 1
            return ans
            
        count = (m + n) // 2
        if (m + n) % 2 == 1:
            count += 1
            
            for _ in range(count-1):
                get_min()
            return get_min()
        else:
            for _ in range(count-1):
                get_min()
            return (get_min() + get_min()) / 2
        
        
        
        