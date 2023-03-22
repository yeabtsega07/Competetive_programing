class Solution:
    def isAdditiveNumber(self, s: str) -> bool:
        n = len(s)
        if n <= 2:
            return False
        
        def backtrack (  index, last = [], valid = False  ):
            
            if index == n:

                return "".join(map(str,last)) == s and len(last) > 2
            
            for i in range(index, n):
                cur = s[index : i + 1]
                   
                if len(last) >= 2:
                    valid = True

                if cur[0] == "0" and len(cur) > 1:
                    continue
                    
                cur = int(cur)
                last.append(cur) 
                
                if  not valid or (valid and  last[-2] + last[-3] == last[-1]) :

                    
                    if backtrack( i + 1, last, valid ):
                        return True
                    
                last.pop()  
                    

            return False

        return backtrack( 0 )
        