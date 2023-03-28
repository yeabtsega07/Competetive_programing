class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        n = len(s)
        track = set()
        
        if len(s) > 12:
            return []
        
        def backtrack (  index, check, k = (len(s) // 4) ):
            
            if index == n:
                if len(check) == 4 and "".join(check) == s:
                    for i in range(4):
                        if len(check[i]) > 3 or not check[i].isdigit() or int(check[i]) > 255  or (check[i][0] == "0" and check[i] != "0"):
                            return 
                    track.add(".".join(check))
                return
            
            for i in range(index, n):
                
                if index - i + 1 > 3:
                    continue
                
                cur = s[index : i + 1]

                check.append(cur)
                backtrack( i + 1, check)
                check.pop()
                
                backtrack( i + 1, check)
                    
        

        backtrack( 0, [] )

        return track       
                
        
        