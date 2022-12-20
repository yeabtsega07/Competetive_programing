class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {}
        for i, char in enumerate(order):
            dict[char] = i
        check = [] 
        for word in words:
            cur = []
            for l in word:
                cur.append(dict[l])
            check.append(cur)
        # print(check)
        for i in range(1, len(words)):
            if check[i - 1] > check[i]:
                return False
        return True   
                      
        