class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        firstHalf = 0
        secondHalf = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        for i,char in enumerate(s):
            if i >= len(s)//2:
                if char in vowels:
                    secondHalf += 1
            else:
                if char in vowels:
                    firstHalf += 1
        

        return firstHalf == secondHalf
            
        