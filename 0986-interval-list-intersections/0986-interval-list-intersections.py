class Solution:
    def intervalIntersection(self, f: List[List[int]], s: List[List[int]]) -> List[List[int]]:
        if not f or not s :
            return []
        res=[]
        pt1,pt2=0,0
        while pt1<len(f) and pt2<len(s):
            intf=f[pt1]
            ints=s[pt2]
            
            if (intf[0]<=ints[1]) and (intf[1]>=ints[0]):
                a=max(ints[0],intf[0])
                b=min(intf[1],ints[1])
                
                res.append([a,b])
                
            if intf[1]<=ints[1]:
                pt1+=1
            else:
                pt2+=1
           
        return res
        