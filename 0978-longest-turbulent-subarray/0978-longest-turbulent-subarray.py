class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        track=[0]*len(arr)
        if len(arr)==1:
            return 1
        elif len(arr)==2 and arr[0]==arr[1]:
            return 1
        
        
        for i in range(len(arr)-1):
            if i==0 and arr[i]!=arr[i+1]:
                track[i]=1
            else:
                if arr[i-1]<arr[i]>arr[i+1] or arr[i-1]>arr[i]<arr[i+1]:
                    track[i]=track[i-1]+1
                elif arr[i]==arr[i-1] and arr[i]==arr[i+1]:
                    track[i]=0
                else:
                    track[i]=1
               
        return max(track)+1        
                
        

                    
            
            
            
            
            
            
        