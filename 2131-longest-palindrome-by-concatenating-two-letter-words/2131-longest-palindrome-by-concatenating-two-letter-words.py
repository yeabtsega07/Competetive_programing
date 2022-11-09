class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        track = Counter(words)
        mid,double,rev = 0,0,0
        
        for char,i  in track.items():
            if char[0] == char[1]:
                double += i//2 *2
                
                if i % 2 == 1:
                    mid = 2
            else:
                rev += min(track[char], track[char[::-1]]) * 0.5
                
        return int(rev) * 4 + double *2 + mid        
        