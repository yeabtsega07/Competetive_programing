class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        @cache
        def recur(rowIndex):
            
            if rowIndex == 0:
                return [1]
            
            arr = []
            for i in range( rowIndex - 1):
                arr.append( recur( rowIndex - 1)[i] + recur(rowIndex - 1)[i + 1])
            
            arr = [1] + arr + [1]
            return arr
        
        return recur(rowIndex)
        