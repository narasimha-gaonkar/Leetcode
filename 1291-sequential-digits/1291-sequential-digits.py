class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(1, 10))
        
        while queue:
            
            num = queue.popleft()
            
            if low <= num <= high:
                res.append(num)
            
            last = num % 10
            
            if last == 9:
                continue
            
            queue.append(num * 10 + last + 1)
            
        # print(res)
        return res
            
            
        