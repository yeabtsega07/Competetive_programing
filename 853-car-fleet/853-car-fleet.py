class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos=[[position[i],speed[i]] for i in range(len(speed))]
        mon_stack=[]
        pos.sort(key=lambda x:x[0], reverse=True)
        for ps in pos:
            time=(target-ps[0])/ps[1]
            mon_stack.append(time) 
            if len(mon_stack)>=2 and mon_stack[-1]<=mon_stack[-2]:
                mon_stack.pop()   
        
        return len(mon_stack)