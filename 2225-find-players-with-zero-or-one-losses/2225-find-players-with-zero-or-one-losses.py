class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        track = defaultdict(int)
        
        for i, pair in enumerate(matches):
            track[pair[0]] += 0
            track[pair[1]] += 1
            
        ans = [[],[]]
        for player in track:
            if track[player] == 0:
                ans[0].append(player)
            elif track[player] == 1:
                ans[1].append(player)
        ans[0] = sorted(ans[0])
        ans[1] = sorted(ans[1])        

        return ans        
        