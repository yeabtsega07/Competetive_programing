class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i, char in enumerate(word):
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]   
            if i == len(word) - 1 :
                cur.is_end = True
                       

    def search(self, word: str) -> bool:
        cur = self.root
        for i, char in enumerate(word):
            if char not in cur.children:
                return False
            cur = cur.children[char] 
            if i == len(word) - 1 and not cur.is_end:
                return False
        return True    

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char] 
        return True 
        

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)