class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.root.is_end = True

    def insert(self, word: str) -> None:
        cur = self.root
        for char in (word):
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char] 
        cur.is_end = True
    
    def isValid(self, word):
        cur = self.root
        
        for char in word:
            
            if char not in cur.children or not cur.children[char].is_end:
                return False
            
            cur = cur.children[char]
        
        return True



class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Solution:
    def longestWord(self, words: List[str]) -> str:
        obj = Trie()
        for word in words:
            obj.insert(word)
        
        words.sort()
        res = ""
        
        for word in words:
            
            if obj.isValid(word) and len(word) > len(res):
                res = word
        
        return res

        
        
        
        
            
            
        