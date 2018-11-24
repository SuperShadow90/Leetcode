--Write a SQL query to get 
-- the second highest salary from the Employee table.


-- Solution 1
SELECT max(salary) as SecondHighestSalary
from employee
where salary < (
select max(salary) 
from employee);


-- Solution 2 (Use offset)
SELECT (
  select distinct Salary from Employee
    order by Salary Desc limit 1 offset 1
)as SecondHighestSalary;