class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def backtrack (  index, check, last = -1  ):
            
            if index == n:

                return check > 1
            
            for i in range(index, n):
                cur = int(s[index : i + 1])

                if last == -1 or last == cur + 1:
                    
                    if backtrack( i + 1, check + 1, cur ):
                        return True
                    
            return False

        return backtrack( 0, 0 )
        