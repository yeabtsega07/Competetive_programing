class Solution:
    def minCost(self, c: str, time: List[int]) -> int:
        """
        color="aaaba"
        start=0
        end=3
        a b
        end-1-start>0
        time=[3, 2 ,1,4,5]
        start=a 0
        end=a 2
        max(time[0])
        start,end=0,0
        sum=0,max=0
        start="a"
        max=max(max,time[i])
        sum+=3
        end+=1
        end="a" i=1
        sum+=2
        end="a" i=2
        sum+1
        end="b"
        start==end
        add this my ans (sum-max)
        start=end
        sum=time[start]
        time O(n) one 
        space o(1)
        c="aabbbcbc"
        c="aaaaa"
        start
        time=[2,3,1,4,5]
        """
        # end=0
        start=0
        sum_,max_=0,0
        res=0
        # while end<len(c):
        for end in range(0,len(c)):
            
            if c[start]==c[end]:
                sum_+=time[end]
                max_=max(max_,time[end])
            else:
                if  end-start-1:
                    res+=(sum_- max_)
                start=end
                sum_=time[end]
                max_=time[end]
            end+=1
        if  end-start-1:
                res+=(sum_- max_)     
            
        return res    
            
        
        