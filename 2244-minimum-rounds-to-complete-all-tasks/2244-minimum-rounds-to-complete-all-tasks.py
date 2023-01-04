class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        ans = 0
        
        for i in count.keys():
            
            while count[i]:
                if count[i] % 2 or count[i] % 3 == 0:
                    count[i] -= 3
                else:
                    count[i] -= 2
                
                if count[i] < 0:
                    return -1
                ans += 1
        
        return ans         
                    
        