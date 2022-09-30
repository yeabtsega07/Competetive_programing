class Solution:
    def canPlaceFlowers(self, flow: List[int], k: int) -> bool:
        track=0
        if k==0:
            return True
        if len(flow)==1 and flow[0]==0 and k<=1:
            return True
        elif len(flow)==1 and flow[0] and k>0:
            return False
        elif len(flow)==1 and flow[0] and k==0:
            return True
        elif len(flow)==1 and flow[0]==0 and k>1:
            return False
            
        for i,n in enumerate(flow):
            if n==1:
                continue
            if i==0 and flow[i+1]==0:
                track+=1
                flow[i]=1
            elif i==len(flow)-1 and flow[i-1]==0:
                track+=1
                flow[i]=1
            elif flow[i-1]==0 and flow[i+1]==0:
                track+=1
                flow[i]=1
            if track==k:
                return True
        return track==k       
                
                
        