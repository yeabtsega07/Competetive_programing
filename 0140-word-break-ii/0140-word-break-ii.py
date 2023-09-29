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

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    
        obj = Trie()    
        for word in wordDict:
            obj.insert(word)
        
        
        result = []
        def backtrack(index ,track):

            if index >= len(s):
                result.append(track[:])
                track = []
                return
                
            for i in range(index, len(s)):
                cur = s[index: i + 1]
                
                if obj.search(cur):
                    track.append(cur)
                    backtrack(i + 1, track)
                    track.pop()
        
        backtrack(0, [])

        ans = []
        for val in result:
            ans.append(" ".join(val))
        
        return ans
            