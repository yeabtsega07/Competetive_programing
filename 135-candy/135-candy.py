class Solution:
    def candy(self, ratings: List[int]) -> int:
        leng=len(ratings)
        count= {i:1 for i in range(leng)}
        for i in range(1,leng): 
            if ratings[i]>ratings[i-1]:
                 count[i]=count[i-1]+1
        for i in range(leng-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                 count[i]=max(count[i],count[i+1]+1)
            

        sum_=0
        for i in range(leng):
            sum_+=count[i]
        return sum_    
        