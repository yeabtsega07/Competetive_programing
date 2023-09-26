
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for i, char in enumerate(word):
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]   
            if i == len(word) - 1 :
                cur.is_end = True
         
        cur.children["*"] = TrieNode()
 
    def search(self, word: str) -> bool:
        cur = self.root
        def recur( index, cur):
            if index == len(word):
                if "*" in cur.children:
                    return True
                return False
            
            if word[index] == ".":
                for child, val in cur.children.items():
                    if recur( index + 1, val ):
                        return True
                return False   
            elif word[index] in cur.children:
                if recur(index + 1, cur.children[word[index]]):
                    return True
            else:
                return False
        return recur(0, cur)
            
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)