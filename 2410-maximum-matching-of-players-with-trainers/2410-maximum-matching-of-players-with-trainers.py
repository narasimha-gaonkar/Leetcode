class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        j = 0
        count = 0
        
        while j < len(trainers) and i < len(players):
            
            if players[i] <= trainers[j]:
                count += 1
                i += 1
            j += 1
        
        return count