class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        track = defaultdict(list)
        
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                track[j].append(strs[i][j])
        
        ans = 0
        for i in track.keys():
            if track[i] != sorted(track[i]):
                ans += 1
        
        return ans
        