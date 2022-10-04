class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones=0
        zeros=0
        count2,count1=0,0
        for i in range(len(s)):
            if s[i]=="1":
                zeros=max(count2,zeros)
                count2=0
                count1+=1
            else:
                ones=max(count1,ones)
                count1=0
                count2+=1
        ones=max(count1,ones) 
        zeros=max(count2,zeros)
        return ones>zeros        
                
                
                
        