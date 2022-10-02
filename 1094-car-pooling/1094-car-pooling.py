class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pre=[0]*1002
        for i in trips:
            pre[i[1]]+=i[0]
            pre[i[2]]-=i[0]
        for i in range(1,1002):
            pre[i]+=pre[i-1]
        for num in pre:
            if num>capacity:
                return False
        return True    
     
        
        
        
        
        