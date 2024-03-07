class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        dx, dy = 0, 1
        x, y = 0, 0
        
        for ins in instructions:
            if ins == 'G':
                x += dx
                y += dy
            elif ins == 'L':
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)
                
            