class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        for i in reversed(range(len(arr))):
            max_val=max(arr[:i+1])
            max_indx=arr.index(max_val)
            arr[:max_indx+1]=reversed(arr[:max_indx+1])
            ans.append(max_indx+1)
            if arr.index(max(arr[:i+1]))== 0:
                max_=max(arr[:i+1])
                arr[:i+1]=reversed(arr[:i+1])
                ans.append(arr.index(max_)+1)
        return ans  
        