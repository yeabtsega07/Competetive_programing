class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.res = 0
    
    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            
            cur = cur.children[char]
        
        cur.count += 1
        cur.isEnd = True
        # print(cur)

    def get_index(self, word, target, startIndex):
        
        for i in range(startIndex, len(word)):
            if word[i] == target:
                return i
        return -1
    
    def get_count(self, word, lastIndex, cur):
        

        if cur.isEnd:

            self.res += cur.count
        
        for char in cur.children:

            index = self.get_index(word, char, lastIndex + 1 )
            
            if index != -1:
                self.get_count(word, index, cur.children[char])
    

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        obj = Trie()
        
        for word in words:
            obj.insert(word)
                 
        obj.get_count(s, -1, obj.root)
        return obj.res
