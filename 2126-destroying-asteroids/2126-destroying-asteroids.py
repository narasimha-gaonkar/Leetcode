class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        stack = []
        
        for asteroid in asteroids:
            
            if asteroid <= mass:
                mass += asteroid
            
                while stack and stack[-1] <= mass:
                        mass += stack.pop()
            else:
                stack.append(asteroid)
            
                
        return not stack