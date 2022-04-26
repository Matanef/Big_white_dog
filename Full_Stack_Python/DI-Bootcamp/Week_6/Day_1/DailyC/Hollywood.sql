-- insert into actors (first_name, last_name, age, number_oscars)
-- VALUES
-- ('Morgan','Freeman','06/01/1937', 1);
-- select avg(number_oscars) AS average_number_oscars from actors;
-- select distinct first_name from actors order by number_oscars desc;
-- select first_name, last_name from actors where age > '01/01/1970';
-- select first_name, last_name from actors where first_name in ('David', 'Morgan', 'Will');

-- update actors set first_name='Maty' where first_name='Matt' and last_name='Damon';
-- select * from actors

-- update actors set number_oscars=4 where first_name='George' and last_name= 'Clooney';
-- select first_name, last_name, number_oscars from actors where first_name='George' and last_name= 'Clooney';

-- alter TABLE actors RENAME COLUMN age TO birthday;
-- alter TABLE actors RENAME COLUMN birthday TO birthdate;
-- select * from actors;

-- delete from actors where first_name= 'Morgan' returning*; 

-- CREATE TABLE movies(
-- movie_id SERIAL,
-- movie_title VARCHAR (50) NOT NULL,
-- movie_story TEXT,
-- actor_playing_id INTEGER,
-- PRIMARY KEY (movie_id),
-- FOREIGN KEY (actor_playing_id) REFERENCES actors (actor_id)
-- );

-- INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
--     ( 'Good Will Hunting', 
--     'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
--     ( 'Oceans Eleven', 
--     'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));

-- select * from movies

-- update actors set first_name='Matt' where first_name='Maty' AND last_name = 'Damon';

-- select * from actors

-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- INNER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id;

-- select * from movies

-- drop table if exists movies;

-- CREATE TABLE movies(
-- movie_id SERIAL,
-- movie_title VARCHAR (50) NOT NULL,
-- movie_story TEXT,
-- actor_playing_id INTEGER,
-- PRIMARY KEY (movie_id),
-- FOREIGN KEY (actor_playing_id) REFERENCES actors (actor_id)
-- );

-- INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
-- ( 'Good Will Hunting', 
-- 'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
-- (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
-- ( 'Oceans Eleven', 
-- 'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
-- (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));

-- select * from movies;

-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- INNER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id;


-- select * from producers

-- drop table if exists producers

-- CREATE TABLE producers(
-- producer_id SERIAL,
-- producer_name VARCHAR (50) NOT NULL,
-- movie_produced_id INTEGER,
-- PRIMARY KEY (producer_id),
-- FOREIGN KEY (movie_produced_id) REFERENCES movies (movie_id)
-- );

-- insert into producers (producer_name, movie_produced_id) values ('Lawrence Bender', 
-- (SELECT movie_id from movies WHERE movie_title='Good Will Hunting'));


select producers.producer_name, movies.movie_title, actors.first_name, actors.last_name
from movies, actors
INNER JOIN producers
ON movies.movie_id = producers.;

select producers.producer_name, movies.movie_title, actors.first_name, actors.last_name
from (producers INNER JOIN movies on movies.movie_id = producers = 



Select table1.ID ,table1.Name
from Table1 inner join Table2 on Table1 .ID =Table2 .ID 
inner join Table3 on table2.ID=Table3 .ID 

