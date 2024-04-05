class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    
        priority_ele = []
        
        for num in arr:
            
            heapq.heappush(priority_ele, (abs(num - x), num))
        res = []
        for _ in range(k):
             res.append(heapq.heappop(priority_ele)[1])
        return sorted(res)