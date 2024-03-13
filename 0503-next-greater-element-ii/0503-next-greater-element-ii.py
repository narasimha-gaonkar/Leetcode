class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        
        p = 1
        n = len(nums)
        res = [-1] * n
        for i in range(n):
            # print('9 Line ', i, nums[i])
            p = i + 1
            if p == n:
                p = 0
            while p < n and p!=i:
                # print('11 Line', nums[p] , nums[i])
                
                if nums[p] > nums[i]:
                    res[i] = nums[p]
                    break
                
                if p == n-1:
                    # print('17 Line', p)
                    p = 0
                else:
                    p += 1
                # print('Line 21->', p)
            
        return res
            
            
        