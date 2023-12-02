class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        check = Counter(chars)
        
        result = 0
        for word in words:
            count = Counter(word)
            flag = True
            for char in count:
                if count[char] > check[char]:
                    flag = False
            result += len(word) if flag else 0
        
        return result