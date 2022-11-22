class Solution:
    def calculate(self, s: str) -> int:
        def comp(ind):
            def change(sign, num):
                
                if sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(stack.pop() //  num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
            
            sign, num, stack = "+", 0, []
            
            while ind < len(s):
                
                if s[ind].isdigit():
                    num = num*10 + int(s[ind])
                
                elif s[ind] in "+-*/":
                    change(sign, num)
                    num, sign = 0, s[ind]
                
                elif s[ind] == "(":
                    num, last = comp(ind + 1)
                    ind = last - 1
                
                elif s[ind] == ")":
                    change(sign, num)
                    return sum(stack), ind + 1
                
                
                ind += 1
            change(sign, num)
            return sum(stack)
        return comp(0)
                    
                    
        