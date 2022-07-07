class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums_removed=0
        mono_stack=[]
        for j in num:
            i=int(j)
            while mono_stack and mono_stack[-1]>i and nums_removed<k:
                mono_stack.pop()
                nums_removed+=1   
            if len(mono_stack)==0 and i==0:
                continue
            else:
                mono_stack.append(i) 
        if nums_removed!=k:
            dif=k-nums_removed
            mono_stack=mono_stack[0:-dif]         
        return "".join(map(str,mono_stack)) or "0"       
                
                