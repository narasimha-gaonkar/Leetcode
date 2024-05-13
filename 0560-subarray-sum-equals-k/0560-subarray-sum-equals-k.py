class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        freq = {0: 1}
        
        prefix_sum = 0
        res = 0
        
        for num in nums:
            
            prefix_sum += num
            
            if prefix_sum - k in freq:
                res += freq[prefix_sum - k]
                
            if prefix_sum not in freq:
                freq[prefix_sum] = 1
            else:
                freq[prefix_sum] += 1
        return res