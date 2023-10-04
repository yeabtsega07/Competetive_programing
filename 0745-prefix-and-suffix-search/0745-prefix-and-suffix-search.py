class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.indexes = set()

class Trie:
    def __init__(self):
        self.prefix = TrieNode()
        self.sufix = TrieNode()
    
    def insert(self, word, index, pre = True):
        if pre:
            cur = self.prefix
        else:
            cur = self.sufix
            word = word[::-1]

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            
            cur = cur.children[char]
            cur.indexes.add(index)
        
        cur.is_end = True

    def starts_with(self, word, pre = True):
        if pre:
            cur = self.prefix
        else:
            cur = self.sufix
            word = word[::-1]
        
        res = set()
        for char in word:
            if char not in cur.children:
                return set()
            
            cur = cur.children[char]
            res = cur.indexes
        
        return res
    
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.cache = {}
        
        for i, word in enumerate(words):
            
            self.trie.insert(word, i)
            self.trie.insert(word, i, False)
            
        
        

    def f(self, pref: str, suff: str) -> int:
        
        if (pref, suff) in self.cache:
            return self.cache[(pref,suff)]
        
        pre  = self.trie.starts_with(pref)
        suf = self.trie.starts_with(suff, False)

        cur = pre.intersection(suf)
        self.cache[(pref, suff)] = max(cur) if cur else -1
        return self.cache[(pref, suff)]

        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)