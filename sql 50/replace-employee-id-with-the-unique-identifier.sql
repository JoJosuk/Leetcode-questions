# Write your MySQL query statement below

select U.unique_id , e.name 
from Employees as E LEFT JOIN EmployeeUNI as U on E.id =U.id;
