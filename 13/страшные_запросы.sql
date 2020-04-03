select concat( a.name, ' ', a.surname, ' starred in the movie "',
f.title, '", directed by ', p.name, ' ', p.surname) as info from
actor_film a_f inner join producer_film p_f using(film_id) join actor a
using(actor_id) join film f using(film_id) join producer p
using(producer_id);
================================================================================
select film.title, count(film.title) from actor_film join actor
using(actor_id) join film using(film_id) group by film.title;
================================================================================
select concat(a.name, ' ', a.surname) as actor, f.title as film,
concat(p.name, ' ', p.surname) as producer from actor_film a_f inner
join producer_film p_f using(film_id) join actor a using(actor_id) join
film f using(film_id) join producer p using(producer_id);
================================================================================
select f.title, concat(p.name, ' ', p.surname) as producer,
string_agg(cast(' ' as varchar(500)), concat(a.name, ' ', a.surname,
',')) as actors from actor_film a_f inner join producer_film p_f
using(film_id) join actor a using(actor_id) join film f using(film_id)
join producer p using(producer_id) where film_id=1 group by
p.producer_id, f.film_id;
================================================================================
select concat(' Фильм ', '"', f.title, '"', ' был снят режиссёром по
имени ', p.name, ' ', p.surname, '. В нём снимались: ',
string_agg(cast(' ' as varchar(500)), concat(a.name, ' ', a.surname,
',')), 'и другие.') from actor_film a_f inner join producer_film p_f
using(film_id) join actor a using(actor_id) join film f using(film_id)
join producer p using(producer_id) where film_id=1 group by
p.producer_id, f.film_id;
================================================================================



