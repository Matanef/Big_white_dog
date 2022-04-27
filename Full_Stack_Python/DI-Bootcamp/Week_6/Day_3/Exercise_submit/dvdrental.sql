-- select *from customer;
-- select (first_name, last_name) as full_name from customer;
-- select create_date from customer;
-- select * from customer order by first_name DESC;
-- select film_id, title, description, release_year, rental_rate from film order by rental_rate ASC;
-- select address, address2, phone from address where district = 'Texas';
-- select * from film where film_id = 15 or film_id = 150;
-- select film_id, title, description, length, rental_rate from film where title = 'Metropolis Coma'
-- select film_id, title, description, length, rental_rate from film where title ilike 'me%';
-- select title, rental_rate from film where rental_rate<=1 limit 10;
-- select title, rental_rate from film where rental_rate<=1 and title NOT (select title, rental_rate from film where rental_rate<=1 limit 10) limit 10;
-- select customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date from customer inner join payment on payment.customer_id = customer.customer_id
-- select city.city, country.country_id, country.country from city inner join country on city.country_id = country.country_id;



-- select * from language;
-- select film.title, film.description,language.name from film inner join language on film.language_id = language.language_id;
-- select film.title,film.description,language.name from film left outer join language on film.language_id = language.language_id;
-- select film.title,film.description,language.name from film full join language on film.language_id = language.language_id

-- create table new_film(
-- new_film_id serial primary key,
-- new_id NUMERIC,
-- new_name VARCHAR(50));

-- insert into new_film(new_id,new_name)
-- values (1,'Lord of the Rings'),(2,'Princess Mononoke'),(3,'Spaceballs')

-- select * from new_film


-- create table customer_review(
-- review_id serial primary key,
-- film_id INTEGER references new_film(new_film_id) on delete cascade,
-- language_id INTEGER references language(language_id),
-- title VARCHAR,
-- score NUMERIC check (score>=0 and score < 11 ),
-- review_text VARCHAR,
-- last_update timestamp without time zone);

-- select * from customer_review
-- drop table new_film cascade
-- select * from customer_review

-- drop table customer_review cascade
-- drop table new_film cascade

-- select * from customer_review

-- insert into customer_review(film_id,language_id,title,score,review_text,last_update)
-- values((select film_id from film where film_id = 1),(select language_id from language where language_id = 1),(select new_name from new_film where new_name='Lord of the Rings'),9.5,'Epic Adventure',(select distinct last_update from film where last_update='2013-05-26 14:50:58.951')),
-- ((select film_id from film where film_id = 2),(select language_id from language where language_id = 3),(select new_name from new_film where new_name='Princess Mononoke'),8.8,'epic story and breathtaking visuals',(select distinct last_update from film where last_update='2013-05-26 14:50:58.951'))
-- select * from customer_review

-- delete from new_film where new_name = 'Princess Mononoke'
select * from customer_review






