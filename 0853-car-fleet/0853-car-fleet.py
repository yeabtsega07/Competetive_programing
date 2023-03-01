class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        track = [ (position[i], speed[i]) for i in range(len(speed))]
        track.sort(reverse = True)
        stack = []
        
        for pos, speed in track:
            
            time = (target - pos) / speed
            stack.append(time)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)