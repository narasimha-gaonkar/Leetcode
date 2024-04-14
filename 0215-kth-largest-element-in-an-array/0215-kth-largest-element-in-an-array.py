class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)

        # remove the topmost item from the heap
        # until k reached.
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
        
        k = len(nums) - k
        def quickselect(l, r):
            p, pivot = l, nums[r]
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[r], nums[p] = nums[p], nums[r]
            
            if p > k:
                return quickselect(l, p-1)
            elif p < k:
                return quickselect(p+1, r)
            else:
                return nums[p]
        
        return quickselect(0, len(nums) - 1)
                
                
            