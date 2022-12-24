class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" == num1 or "0" == num2:
            return "0"
        
        ans = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                ans[i + j] += (int(num1[i]) * int(num2[j]))
                ans[i + j + 1] += (ans[i + j] // 10)
                ans[i + j] %= 10
        
        indx, ans = 0, ans[::-1]
        while indx < len(ans) and ans[indx] == 0:
            indx += 1
        
        ans = map(str, ans[indx:])
        return "".join(ans)