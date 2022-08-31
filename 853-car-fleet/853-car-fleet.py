class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos=[[position[i],speed[i]] for i in range(len(speed))]
        mon_stack=[]
        pos.sort(key=lambda x:x[0])
        for ps in pos:
            time=(target-ps[0])/ps[1]
            while mon_stack and mon_stack[-1]<=time:
                mon_stack.pop()
            mon_stack.append(time)    
        
        return len(mon_stack)