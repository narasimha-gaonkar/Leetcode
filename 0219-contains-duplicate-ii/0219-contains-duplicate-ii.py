class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        map = {}
        
        for i, ele in enumerate(nums):
            # print(map)
            if ele in map:
                if i- map[ele] <= k:
                    return True
                else:
                    map[ele] = i
            else:
                map[ele] = i

        return False
                    
        