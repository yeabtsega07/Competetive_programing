class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack, res = [], []
        pt =0
        
        for i in range(1,n+1):
            
            stack.append(i)
            res.append("Push")
            
            if stack[pt] == target[pt]:
                pt += 1
            else:
                stack.pop()
                res.append("Pop")
            
            if stack == target :
                return res
            
            
        