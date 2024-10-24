class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        snum = list(set(nums))
        if len(snum) == 1 and snum[0] == 0:
            return 0
        elif snum[0] == 0:
            return len(snum) - 1
        else:
            return len(snum)
        
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
        