class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return
        
        telephone = {
            "2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], 
            "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]
        }
        
        res = []
        
        def backtrack(index = 0, track = []):
            
            if index >= len(digits):
                res.append("".join(track))
                
                return
            
            number = digits[index]
            for char in telephone[number]:
                
                track.append(char)
                backtrack(index + 1, track)
                track.pop()
        
        backtrack()
        
        return res
                
        