class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[0])  # Sort by start point

        arrow_count = 1
        min_common_point = points[0][1]  # Initialize with end point of first interval

        for start, end in points[1:]:
            if start > min_common_point:  # Current interval starts after common point
                arrow_count += 1
                min_common_point = end
            else:
                min_common_point = min(min_common_point, end)  # Update common point

        return arrow_count
                