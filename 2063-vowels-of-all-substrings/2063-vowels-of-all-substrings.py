class Solution:
    def countVowels(self, word: str) -> int:
        
        vowels = set(['a', 'e', 'i', 'o','u'])
        nums = []
        for char in word:
            if char in vowels:
                nums.append(1)
            else:
                nums.append(0)
        
        res, n = 0, len(word)
        for i in range(n):
             res += nums[i] * (i + 1) * (n - i)
        
        return res