-- Write your PostgreSQL query statement below
select distinct viewer_id id
  from views
 where ( author_id = viewer_id )
 order by id asc