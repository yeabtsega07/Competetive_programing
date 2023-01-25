class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans, max_ = [], -1
        
        for i in reversed(range(len(arr))): 
            
            ans.append(max_)
            max_ = max(max_, arr[i])
        
        return ans[::-1]
            
        
        
        