class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxLength, self.left, self.right = 0, 0, 0
        
        
        def recur (l,r):
            if l >= 0 and r < len(s) and s[l] == s[r]:
                
                if self.maxLength < r-l+1:
                    self.maxLength, self.left, self.right = r-l+1, l, r
                return recur(l-1, r+1)
        
        for i in range(len(s)-1):
            recur(i,i)
            recur(i,i+1)
        return s[self.left:self.right+1]  
    
    """
    babad
    01234
    0
    
    """

                
            
        