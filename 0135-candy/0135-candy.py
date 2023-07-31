class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        count= {i:1 for i in range(len(ratings))}
        
        for i in range(1, len(ratings)): 
            if ratings[i] > ratings[i - 1]:
                 count[i] = count[i - 1] + 1
                    
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                 count[i] = max(count[i], count[i + 1] + 1)
            

        res = 0
        for i in range(len(ratings)):
            res += count[i]
        return res    
        