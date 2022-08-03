class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        list1=[]
        def merge(lft,rgt):
            new_list=[]
            i,j=0,0
            while len(new_list)<(len(lft)+len(rgt)):
                if lft[i]<=rgt[j]:
                    new_list.append(lft[i])
                    i+=1
                else:
                    new_list.append(rgt[j])
                    j+=1
                if j>=len(rgt):
                    new_list+=lft[i:]
                elif i>=len(lft):
                    new_list+=rgt[j:]          
            return new_list 
        def mergesort(list_):
            if len(list_)==1:
                return list_
            half=len(list_)//2
            lft=list_[:half]
            rgt=list_[half:]  
            lft=mergesort(lft)
            rgt=mergesort(rgt)
            return merge(lft,rgt)
        num=mergesort(nums)
        for i in range(len(num)):
            if num[i]==target:
                list1.append(i)
        return list1       
