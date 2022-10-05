class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        track={}
        for i,char in enumerate(s):
            track[char]=i
        
        st,end=0,0
        res=[]
        for i,char in enumerate(s):
            st+=1
            if track[char]>end:
                end=track[char]
            if i==end:
                res.append(st)
                st=0
        return res       
                