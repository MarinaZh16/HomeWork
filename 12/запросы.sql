select actor.name as actor_name, actor.surname as actor_surname,
film.title as film, producer.name as producer_name, producer.surname as
producer_surname from actor_film inner join producer_film using(film_id)
join actor using(actor_id) join film using(film_id) join producer
using(producer_id);
===========================================================================
select distinct actor.name as actor_name, actor.surname as actor_surname
from actor_film join actor using(actor_id) where actor.name='Том';
===========================================================================
select distinct film.title as film, producer.name as producer_name,
producer.surname as producer_surname from producer_film join film
using(film_id) join producer using(producer_id) where
producer.surname='Нолан';
===========================================================================
select actor.name as actor_name, actor.surname as actor_surname,
film.title as film from actor_film join actor using(actor_id) join film
using(film_id); ИЛИ select actor.name as actor_name, actor.surname as
actor_surname, film.title as film from actor_film join actor on
actor_film.actor_id=actor.actor_id join film on
actor_film.film_id=film.film_id;
===========================================================================
select actor.name as actor_name, actor.surname as actor_surname,
producer.name as producer_name, producer.surname as producer_surname
from actor_film join producer_film using(film_id) join actor
using(actor_id) join producer using(producer_id);
===========================================================================
select film.title as film, producer.name as producer_name,
producer.surname as producer_surname from producer_film join film
using(film_id) join producer using(producer_id);
===========================================================================
select actor.name as actor_name, actor.surname as actor_surname,
film.title as film, producer.name as producer_name, producer.surname as
producer_surname from actor_film inner join producer_film using(film_id)
join actor using(actor_id) join film using(film_id) join producer
using(producer_id) order by actor.surname;
===========================================================================
select count(distinct actor.surname) as actor_surname from actor_film
join actor using(actor_id) join film using(film_id);
===========================================================================
update actor set name=surname, surname=name;
===========================================================================
alter table actor rename column name to surname_1;
===========================================================================
alter table actor rename column surname to name;
===========================================================================
alter table actor rename column surname_1 to surname;
===========================================================================
select * from actor limit 3;
===========================================================================
select * from actor limit 3 offset 3;
===========================================================================
select title from film fetch first row only;
===========================================================================
select title from film fetch first 3 row only;
