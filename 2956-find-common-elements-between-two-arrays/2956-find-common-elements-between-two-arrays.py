class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # hash = defaultdict(int)
        
        hash = {}
        
        for ele in nums1:
            
            if ele in hash:
                
                hash[ele] =  hash[ele] + 1
            else:
                hash[ele] = 1
            
        print(hash)
        res = [0, 0]
        
        for ele in nums2:
            if ele in hash:
                res[1] = res[1] + 1
                res[0] = res[0] + hash[ele]
                hash[ele] = 0
                # res.append(ele)
        return res
            
        