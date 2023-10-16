class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        v4 = queryIP.split(".")
        v6 = queryIP.split(":")

        if len(v4) == 4:
            valid = 1
            for x in v4:
                if not x or (x != "0" and x[0] == "0") or not x.isdigit():
                    valid = 0
                    break
                if not (0 <= int(x) <= 255):
                    valid = 0
                    break
            
            if valid: return "IPv4"
                
        elif len(v6) == 8:
            valid = 1
            for x in v6:
                if not (1 <= len(x) <= 4):
                    valid = 0
                    break
                check = 1
                for char in x:
                    if not char.isdigit() and not (ord("a") <= ord(char) <= ord("f") or ord("A") <= ord(char) <= ord("F")):
                        valid = 0
                        check =0
                        break
                if not check: break                    
            if valid: return "IPv6"
        
        return "Neither"
        
            
                
        