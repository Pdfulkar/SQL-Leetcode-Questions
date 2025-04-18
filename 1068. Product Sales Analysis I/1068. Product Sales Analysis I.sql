-- Write your PostgreSQL query statement below
select p.product_name, s.year, s.price
from Product p
Right join sales s
on (s.product_id = p.product_id )