class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        track = defaultdict(list)
        
        for edge in edges:
            
            track[edge[0]].append(edge[1])
            track[edge[1]].append(edge[0])
        
        res = [0, 0]
        for key in track.keys():
            
            if res[0] < len(track[key]):
                res = [len(track[key]), key]
        
        return res[1]
        