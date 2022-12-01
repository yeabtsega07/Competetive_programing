class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        firstHalf = []
        secondHalf = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i,char in enumerate(s):
            if i >= len(s)//2:
                if char in vowels:
                    secondHalf.append(char)
            else:
                if char in vowels:
                    firstHalf.append(char)
        
        # print(firstHalf, secondHalf)
        return len(firstHalf) == len(secondHalf)
            
        