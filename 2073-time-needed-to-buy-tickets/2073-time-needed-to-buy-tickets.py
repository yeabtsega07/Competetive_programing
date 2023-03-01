class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        count = 0
        
        for i, ticket in enumerate(tickets):
            
            if i < k:
                count += min(ticket, tickets[k])
                
            elif i > k:
                count += min(ticket, tickets[k] - 1)
            
            else:
                count += ticket
        
        return count 
