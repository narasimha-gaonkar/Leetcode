class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def kdist(temp_k):
            freq = {}
            count = 0
            l = 0
            for r in range(len(nums)):

                freq[nums[r]] = freq.get(nums[r], 0) + 1
                # print(freq, count)
                while len(freq) > temp_k:

                    freq[nums[l]] = freq[nums[l]] - 1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l += 1
                count += r - l + 1

            return count
        return kdist(k) - kdist(k-1)
                
        