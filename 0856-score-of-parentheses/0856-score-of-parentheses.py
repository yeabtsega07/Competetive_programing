class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count, stack = 0, []
        
        for char in s:
            
            if char == "(":
                stack.append(count)
                count = 0
            else:
                count = stack.pop() + max(count * 2, 1)
        
        return count

        