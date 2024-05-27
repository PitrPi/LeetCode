select case when max(ranks) < 2 then null else salary end as SecondHighestSalary from (
select salary,
dense_rank() over (order by salary desc) as ranks
from Employee
) x
where ranks = 2
