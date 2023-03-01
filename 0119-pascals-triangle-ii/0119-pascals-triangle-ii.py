class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        # @cache
        def recur(rowIndex):
            
            if rowIndex == 0:
                return [1]
            
            arr, cur = [], recur(rowIndex - 1) 
            for i in range( rowIndex - 1):
                
                arr.append( cur[i] + cur[i + 1])
            
            arr = [1] + arr + [1]
            return arr
        
        return recur(rowIndex)
        