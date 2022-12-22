class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        cur = ""
        
        for i, char in enumerate(command):
            if char ==  "(":
                cur += char
                continue
            if char == ")":
                if cur == "(":
                    ans += "o"
                else:
                    ans += "al"
                cur = ""  
                continue
            if not cur and char != ")" and char != "(":
                ans += char
            else:
                cur += char
        
        return ans
                