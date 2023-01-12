class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        track = Counter(words[0])
        
        for i  in range(1, len(words)):
            check = Counter(words[i])
            for char in track:
                track[char] = min(track[char], check[char])
        

        ans = []
        for item in track.items():
            for i in range(item[1]):
                ans.append(item[0])
        
        return ans
        