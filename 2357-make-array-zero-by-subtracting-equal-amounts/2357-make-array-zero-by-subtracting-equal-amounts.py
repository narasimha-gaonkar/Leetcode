class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        snum = list(set(nums))
        
        prevSum = 0
        
        count = 0
        snum.sort()
        
        for num in snum:
            
            if num == 0:
                continue
            else:
                prevSum += num - prevSum
                count += 1
                
        
        return count
        