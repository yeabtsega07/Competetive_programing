class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
                
        l,r,res= 0,0,0 
        
        while l<len(pos) and r<len(neg):
            
            nums[res] = pos[l]
            res += 1
            l += 1
            
            nums[res] = neg[r]
            res += 1
            r += 1
        
        return nums    
        
        