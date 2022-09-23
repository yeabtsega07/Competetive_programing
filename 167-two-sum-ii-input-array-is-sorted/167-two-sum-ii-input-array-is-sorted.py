class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            lft,rgt=0,len(numbers)-1
            while lft<rgt:
                if numbers[lft]+numbers[rgt]==target:
                    return [lft+1,rgt+1]
                if numbers[lft]+numbers[rgt]>target:
                    rgt-=1
                else:
                    lft+=1
 
                    
         
        