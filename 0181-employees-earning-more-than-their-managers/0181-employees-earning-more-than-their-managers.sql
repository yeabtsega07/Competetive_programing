# Write your MySQL query statement below
Select x.name as 'Employee' from Employee as x join Employee as y where x.managerId = y.Id And x.Salary > y.Salary