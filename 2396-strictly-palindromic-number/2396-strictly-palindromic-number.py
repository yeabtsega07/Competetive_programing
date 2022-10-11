class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        left,right=0,n-2
        
        while left<=right:
            
            check1=bin(left)[2:]
            check2=bin(right)[2:]
            
            d=len(check1)//2
            temp=reversed(check1[d:])
            if d%2!=0 and check1[:d+1]!=temp:
                return False
            elif d%2==0 and check1[:d]!=temp:
                return False
            
            d=len(check2)//2
            temp=reversed(check2[d:])
            if d%2!=0 and check2[:d+1]!=temp:
                return False
            elif d%2==0 and check2[:d]!=temp:
                return False
            
            left+=1
            right-=1
        return True     
        