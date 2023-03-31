class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 2:
            return 0
        
        check = [1] * n
        check[0] = check[1] = 0
        
        i = 2 
        
        while i * i < n:
            
            if check[i]:
                
                j = i * i
                
                while j < n:
                    
                    check[j] = 0
                    j += i
            i += 1
        
        
        count = 0
        for num in check:
            if num:
                count += 1
        
        return count
            
                
                
        