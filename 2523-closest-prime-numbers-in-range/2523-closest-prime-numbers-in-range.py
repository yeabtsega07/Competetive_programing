class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
                        
        check = [0] * (right + 1)
        check[0] = check[1] = 1
         
        i = 2
        
        while i * i <= right:
            
            if not check[i]:
                
                j = i * i
                
                while j <= right:
                    
                    check[j] = 1
                    j += i
                    
            i += 1
        
        pre = 0
        minVal = []
        for i in range(left, right + 1):

            if not check[i] and not pre:
                pre = i
            elif not check[i]:
                if not minVal:
                    minVal = [pre, i]
                else:
                    minVal = [pre, i] if minVal[1] - minVal[0] > i - pre else minVal
                pre = i
                
                
        
        return [-1,-1] if not minVal else minVal
        
            
            
        