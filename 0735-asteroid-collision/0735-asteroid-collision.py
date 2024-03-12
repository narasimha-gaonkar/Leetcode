class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
                continue
            while stack:
                if stack[-1] > 0 and asteroid < 0:
                    if stack[-1] > abs(asteroid):
                        break
                    elif stack[-1] == abs(asteroid):
                        stack.pop()
                        break
                    else:
                        stack.pop()
                        if not stack:
                            stack.append(asteroid)
                            break
                else:
                    stack.append(asteroid)
                    break    
        return stack
                        
                    
                    