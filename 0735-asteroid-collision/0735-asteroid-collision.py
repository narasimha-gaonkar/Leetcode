class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        # stack.append(asteroids.pop(0))
        
        for asteroid in asteroids:
            # print(asteroid, stack)
            if not stack:
                stack.append(asteroid)
                continue
            while stack:
                if stack[-1] < 0 and asteroid < 0:
                    stack.append(asteroid)
                    break
                elif stack[-1] > 0 and asteroid > 0:
                    stack.append(asteroid)
                    break
                elif stack[-1] < 0 and asteroid > 0:
                    stack.append(asteroid)
                    break
                else:
                    # print('here', stack[-1],asteroid )
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
                            # print('not here', stack,asteroid )
                            
                        
        return stack
                        
                    
                    