class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        
        def subarrayWithMaxKDistinct(n_ele):
            count = 0
            freq = defaultdict(int)
            start = 0
            
            for end in range(len(nums)):
                
                freq[nums[end]] += 1
                
                while len(freq) > n_ele:
                    freq[nums[start]] -= 1
                    if  freq[nums[start]] == 0:
                        del freq[nums[start]]
                    start += 1
                count += end - start + 1
                
            return count
        return subarrayWithMaxKDistinct(k) - subarrayWithMaxKDistinct(k - 1)