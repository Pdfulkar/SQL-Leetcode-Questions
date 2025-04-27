select  p.project_id, round(avg(experience_years),2) as average_years
from employee e
left join project p 
on e.employee_id = p.employee_id
where project_id is NOT NULL
group by project_id