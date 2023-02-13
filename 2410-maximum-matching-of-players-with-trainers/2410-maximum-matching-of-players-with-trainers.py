class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res, right = 0 , 0
        for left in range(len(players)):

            if right >= len(trainers):
                break
            
            
            while right < len(trainers) - 1 and trainers[right] < players[left]:
                right += 1

            if trainers[right] >= players[left]:
                res += 1
                right += 1
        
        return res
        