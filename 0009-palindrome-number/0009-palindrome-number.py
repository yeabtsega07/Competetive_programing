class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        check = ""
        for i in range(len(x) - 1, -1, -1):
            check += x[i]
        return check == x   
            
        

        