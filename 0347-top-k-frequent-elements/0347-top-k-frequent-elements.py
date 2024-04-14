class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        
        unique_nums = list(freq.keys())
        n = len(unique_nums)
        k = n - k
        
        def quickSelect(l , r):
            pivot = freq[unique_nums[r]]
            p = l
            
            for i in range(l, r):
                if freq[unique_nums[i]] <= pivot:
                    unique_nums[p], unique_nums[i] = unique_nums[i], unique_nums[p]
                    p += 1
            unique_nums[r], unique_nums[p] = unique_nums[p], unique_nums[r]
            
            if p > k: return quickSelect(l, p-1)
            elif p < k: return quickSelect(p+1, r)
            else:
                return
        
        quickSelect(0, n -1)
        return unique_nums[k:]
        
            
            
            
            
            
        