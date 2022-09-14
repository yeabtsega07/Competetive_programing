class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        rear,top=len(people)-1,0
        boat=0
        while top<=rear:
            if people[rear]+people[top]<=limit:
                rear-=1
                top+=1
            else:
                rear-=1
            boat+=1
        return boat    
                        
        