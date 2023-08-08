# Write your MySQL query statement below
Select Person.email From Person Group by Person.email Having Count(*) > 1;