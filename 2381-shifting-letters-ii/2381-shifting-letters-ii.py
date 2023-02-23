class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        track = [0] * (len(s) + 1)
        
        for shift in shifts:
            start = shift[0]
            end = shift[1]
            direction = shift[2]
            
            if direction:
                track[start] += 1
                track[end + 1] -= 1 
            else:
                track[start] -= 1
                track[end + 1] += 1
                
        res, runSum = [], 0
        
        for i , char in enumerate(s):
            
            runSum += track[i]
            character = chr(ord("a") + (ord(char) - ord("a") + runSum) % 26)
            res.append(character)
            
        return "".join(res)    