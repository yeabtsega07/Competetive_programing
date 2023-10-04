class TrieNode:
    def __init__ (self):
        self.children = {}
        self.is_end = False
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            
            cur = cur.children[char]
            cur.count += 1
        
        cur.is_end = True
    
    def search(self, word):
        cur = self.root
        count = 0
        
        for char in word:
            if char not in cur.children:
                return count
            
            cur = cur.children[char]
            
            count += cur.count
        
        return count
        


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        obj = Trie()
        
        for word in words:
            obj.insert(word)
        

        result = []
        for word in words:
            result.append(obj.search(word))
        
        return result
        
        
        
        