class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        for i,num in enumerate(customers):
            if grumpy[i] == 0:
                ans += num
        print(ans)
        left,curSum = 0,0
        max_ = 0
        for right,num in enumerate(customers):
            
            if grumpy[right] == 1:
                curSum +=num
        
            if (right - left + 1) > minutes:
                if grumpy[left] == 1:
                    curSum -= customers[left]
                left += 1    
            
            max_ = max(curSum , max_)
           
        return ans + max_    
        