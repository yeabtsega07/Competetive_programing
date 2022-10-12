class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        track=[]
        for i,p in enumerate(points):
            track.append([sqrt(p[0]**2+p[1]**2),i])
            
        track.sort(key=lambda x:x[0])
        res=[]
        i=0
        while i<k:
            res.append(points[track[i][1]])
            i+=1
        return res
        