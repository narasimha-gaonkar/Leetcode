class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        x, y = newInterval
        
        # intervals[0][0] = min(newInterval[0], intervals[0][0])
        print(x, y)
        
        
        while intervals:
            start, end = intervals.pop(0)
            
            if not res and y < start:
                res.append(newInterval)
                res.append([start, end])
                res.extend(intervals)
                return res
                           
            if y < start:
                res.append(newInterval)
                res.append([start, end])
                res.extend(intervals)
                return res
            elif x <= end:
                maxx = max(end, y)
                minn = min(start, x)
                print('line 10 ', maxx, start, end)
                while intervals and  maxx >= intervals[0][0]:
                    print('line 12', intervals[0] , maxx)
                    maxx = max(intervals.pop(0)[1], maxx)
                print('line 13', maxx, start, end)
                res.append([minn, maxx])
                
                res.extend(intervals)
                return res
    
            else:
            
                res.append([start, end])
                print('else proper', res)
        # else:
        res.append(newInterval)
        return res
            