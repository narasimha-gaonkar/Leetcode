class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        min_length = n + 1
        
        prefix_sum = [0]
        
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        dq = deque()
        
        for i in range(n + 1):
            
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            dq.append(i)
    
        return -1 if min_length == n + 1 else min_length
                                                     
                                                     