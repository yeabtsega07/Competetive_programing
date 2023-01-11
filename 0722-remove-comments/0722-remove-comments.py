class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        flag = False
        check = ""
        for cmd in source:
            if not flag:
                check = ""
            i = 0
            while i < len(cmd):
                if not flag:
                    if i+1 < len(cmd) and cmd[i] == "/" and cmd[i+1] == "/":
                        break
                    elif i+1 < len(cmd) and cmd[i] == "/" and cmd[i+1] == "*":
                        i += 2
                        flag = True
                    else:
                        check += cmd[i]
                        i += 1
                else:
                    if i+1 < len(cmd) and cmd[i] == "*" and cmd[i+1] == "/":
                        flag = False
                        i += 2
                    else: 
                        i += 1
            
            if not flag and len(check) > 0:
                ans.append(check)      

        return ans