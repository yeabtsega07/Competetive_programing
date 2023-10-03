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



class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Solution:
    def longestWord(self, words: List[str]) -> str:
        obj = Trie()
        for word in words:
            obj.insert(word)

        track, length = [], 0
        stack = [(obj.root, [""])]
        while stack:
            node, cur = stack.pop()
            if not node.is_end:
                continue
                
            if len(cur) >= length:
                track = cur
                length = len(cur)
            
            for val in range(26):
                char = chr(val + 97)
                if char in node.children:
                    stack.append((node.children[char], cur + [char]))
        
        return "".join(track)
        
        
        
        
            
            
        