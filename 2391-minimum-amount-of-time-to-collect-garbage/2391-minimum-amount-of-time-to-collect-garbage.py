class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        def count(s, char):
            cnt = 0
            for c in s:
                
                if c ==char:
                    cnt += 1
            return cnt        
        
        def helper(char):
            
            res, lst = 0,-1
            for i,s in enumerate(garbage):
                
                if count(s , char) and i == 0:
                    lst = i
                    res += count(s,char)
                    
                if i > 0:
                    res += travel[i-1]
                    if count(s, char):
                        
                        lst = i
                        res += count(s , char)
            return (res, lst)
        
        g = helper("G")
        p = helper("P")
        m = helper("M")
        ans = 0

        for i in range(1, len(travel)):
            travel[i] += travel[i-1]
            
        if (g[1] < len(garbage)- 1) and g[1] != -1:
            if g[1] == 0:
                ans += (g[0] - travel[len(travel) - 1])
            else:    
                ans += (g[0] - (travel[len(travel) - 1] - travel[g[1] - 1]))
        elif g[1] ==  len(garbage) - 1:
            ans += g[0]        
                    
        if (p[1] < len(garbage)- 1) and p[1] != -1:
            if p[1] == 0:
                ans += (p[0] - travel[len(travel) - 1])
            else:    
                ans += (p[0] - (travel[len(travel) - 1] - travel[p[1] - 1]))
                       
        elif p[1] == len(garbage)- 1:
            ans += p[0]
        
        if (m[1] < len(garbage)- 1) and m[1] != -1:
            if m[1] == 0:
                ans += (m[0] - travel[len(travel) - 1])
            else:    
                ans += (m[0] - (travel[len(travel) - 1] - travel[m[1] - 1]))        
        elif m[1] == len(garbage)- 1:
            
            ans += m[0]  
        
        return ans            
                
                
            
        