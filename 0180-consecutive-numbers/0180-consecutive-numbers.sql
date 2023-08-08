# Write your MySQL query statement below
SELECT DISTINCT a.Num AS ConsecutiveNums FROM Logs a, Logs b, Logs c WHERE a.Id = b.Id - 1 AND b.Id = c.Id - 1 AND a.Num = b.Num AND b.Num = c.Num ;