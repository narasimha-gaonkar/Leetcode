class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        if deadends == target:
            return -1
        if '0000' in deadends:
            return -1
        
        queue = deque(['0000'])
        min_moves = 0
        
        while queue:
            for _ in range(len(queue)):
                
                state = queue.popleft()
                
                if state == target:
                    return min_moves
                
                for i in range(4):
                    for j in [-1, 1]:
                        new_state = str((int(state[i]) + j ) % 10)
                        new_state = state[:i] + new_state + state[i+1:]
                        
                        if new_state not in deadends:
                            deadends.add(new_state)
                            queue.append(new_state)
            min_moves += 1
            
        return -1