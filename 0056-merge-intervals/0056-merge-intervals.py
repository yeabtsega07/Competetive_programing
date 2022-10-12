class Solution:
    def merge(self, i: List[List[int]]) -> List[List[int]]:
        i.sort(key=lambda x:x[0])
        res=[i[0]]
        
        for itv in i:
            if res[-1][1]>=itv[0]:
                res[-1]=[res[-1][0],max(res[-1][1],itv[1])]
            else:
                 res.append(itv)
        return res                 

                
                            
        