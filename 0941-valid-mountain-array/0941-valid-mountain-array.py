class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        if n < 3:
            return False
        
        count = []
        for i in range(1, n):
            
            if arr[i - 1] < arr[i]:
                count.append(-1)
            elif arr[i - 1] > arr[i]:
                count.append(1)
            else:
                return False
        
        change = 0
        for i in range(1,  n - 1):
            
            if count[i - 1] != count[i]:
                change += 1
        
        return change == 1 and count[0] == -1
            
                
        
        
        