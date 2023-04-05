class Solution:
    def minSteps(self, n: int) -> int:
        
        prime  =  2
        fact = [] 
        
        while prime * prime <= n :
            
            while n % prime == 0 :
                
                fact.append(prime)
                n = n // prime
                        
            prime += 1
        
        if n > 1:
            fact.append(n)
        

        return sum( fact )
        