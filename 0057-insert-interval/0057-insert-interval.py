class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        x, y = newInterval
        
        inserted = False
        for interval in intervals:
            
            if interval[1] < x:
                res.append(interval)
            elif interval[0] > y:
                if not inserted:
                    res.append([x, y])
                    inserted = True
                res.append(interval)
            else:
                x = min(x, interval[0])
                y = max(y, interval[1])
        
        if not inserted:
            res.append([x, y])
        return res
        
        
#         if not intervals:
#             return [newInterval]
#         res = []
#         x, y = newInterval
        
#         while intervals:
#             start, end = intervals.pop(0)
            
#             if not res and y < start:
#                 res.append(newInterval)
#                 res.append([start, end])
#                 res.extend(intervals)
#                 return res
                           
#             if y < start:
#                 res.append(newInterval)
#                 res.append([start, end])
#                 res.extend(intervals)
#                 return res
#             elif x <= end:
#                 maxx = max(end, y)
#                 minn = min(start, x)
                
#                 while intervals and  maxx >= intervals[0][0]:
                    
#                     maxx = max(intervals.pop(0)[1], maxx)
                    
#                 res.append([minn, maxx])
                
#                 res.extend(intervals)
#                 return res
    
#             else:
            
#                 res.append([start, end])

#         res.append(newInterval)
#         return res
            