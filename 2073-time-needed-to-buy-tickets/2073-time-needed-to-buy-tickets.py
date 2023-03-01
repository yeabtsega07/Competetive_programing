class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        count = 0
        
        while tickets[k]:
            
            for i, ticket in enumerate(tickets):
                
                if ticket  != 0:
                    tickets[i] -= 1
                    count += 1 
                
                if tickets[i] == 0 and i == k:
                    break
            
        return count    