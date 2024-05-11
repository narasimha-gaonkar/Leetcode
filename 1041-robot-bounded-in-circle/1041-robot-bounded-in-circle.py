class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        dx, dy = 0, 1
        x, y = 0, 0
        
        for direction in instructions:
            if direction == 'L':
                dx, dy = -dy, dx
            elif direction == 'R':
                dx, dy = dy, -dx
            else:
                x += dx
                y += dy
        
        # print(x, y)
        
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)