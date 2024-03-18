class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        x, y = newInterval

        # Add intervals before newInterval
        while intervals and intervals[0][1] < x:
            res.append(intervals.pop(0))

        # Merge overlapping intervals
        while intervals and intervals[0][0] <= y:
            x = min(x, intervals[0][0])
            y = max(y, intervals[0][1])
            intervals.pop(0)

        res.append([x, y])  # Add merged interval

        # Add remaining intervals
        res.extend(intervals)

        return res
        
        # if not intervals:
            # return [newInterval]
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
            