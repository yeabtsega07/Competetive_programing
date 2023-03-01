class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        def reverse ( index ):
            
            if index >= n // 2:
                return
            
            s[index], s[n - index - 1] = s[ n - index - 1], s[ index]
            reverse(index + 1)
        
        reverse(0)
        
            
            
        
        
        
        