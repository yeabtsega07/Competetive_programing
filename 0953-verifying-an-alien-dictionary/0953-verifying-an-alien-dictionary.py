class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        check = [] 
        for word in words:
            cur = []
            for l in word:
                for i, char in enumerate(order):
                    if char == l:
                        cur.append(i)
            check.append(cur)
        # print(check)
        for i in range(1, len(words)):
            if check[i - 1] > check[i]:
                return False
        return True   
                      
        