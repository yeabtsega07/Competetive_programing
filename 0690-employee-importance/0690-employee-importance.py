"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        self.ans = 0
        
        def dfs ( employee, visited = set() ):
            
            visited.add(employee)
            self.ans += employee.importance
            
            for sub in employee.subordinates:
                
                for employee in employees:
            
                    if employee.id == sub:
                        sub = employee
                        break
                
                if sub not in visited:
                    
                    dfs( sub, visited)
        
        for employee in employees:
            
            if employee.id == id:
                
                dfs( employee )
                break
        
        return self.ans
            