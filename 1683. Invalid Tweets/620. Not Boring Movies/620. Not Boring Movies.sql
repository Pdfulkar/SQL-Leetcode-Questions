select id, movie, description, rating
from cinema
having mod(id,2)=1 and description != "boring"
order by rating desc