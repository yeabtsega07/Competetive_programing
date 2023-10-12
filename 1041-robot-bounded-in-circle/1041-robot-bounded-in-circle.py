class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        cur, point = "N", (0,0)
    
        for char in (instructions * 4):
            
            if char == "G" and cur == "N":
                point = (point[0], point[1] + 1)
            elif char == "G" and cur == "E":
                point = (point[0] + 1, point[1])
            elif char == "G" and cur == "W":
                point = (point[0] - 1, point[1])
            elif char == "G" and cur == "S":
                point = (point[0], point[1] - 1)
            
            if char == "L" and cur == "S":
                cur = "E"
            elif char == "L" and cur == "N":
                cur = "W"
            elif char == "L" and cur == "W" :
                cur = "S"
            elif char == "L" and cur == "E":
                cur = "N"
            
            if char == "R" and cur == "N" :
                cur = "E"
            elif char == "R" and  cur == "S":
                cur = "W"
            elif char == "R" and cur == "W" :
                cur = "N"
            elif char == "R" and cur == "E":
                cur = "S"
            
        
        return point == (0,0)
           
        