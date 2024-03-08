class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
    
        freq = {}
        
        max_occ = 0
        
        for i in nums:
            
            freq[i] = freq.get(i, 0) + 1
            max_occ = max(max_occ, freq[i])
            
        return sum(list(filter(lambda value: value == max_occ, freq.values())))