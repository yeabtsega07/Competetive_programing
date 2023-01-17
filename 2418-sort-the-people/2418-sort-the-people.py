class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        track = defaultdict(list)
        max_ = 0
        
        for i, name in enumerate(names):
            track[heights[i]].append(name)
            max_ = max(max_, heights[i])
        
        ans = []
        # print(track, max_)
        for i in reversed(range(max_ + 1)):
            if i in track:
                for x in track[i]:
                    ans.append(x)
        
        return ans
        
        
        