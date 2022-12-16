class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for i in range (len(matrix[0])):
            cur = []
            for j in range(len(matrix)):
                cur.append(matrix[j][i])
            ans.append(cur)
        
        return ans
                
            