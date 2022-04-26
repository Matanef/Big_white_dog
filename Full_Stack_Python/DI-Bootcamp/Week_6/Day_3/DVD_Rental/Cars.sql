-- create table colors (
-- color_id serial primary key,
-- name varchar (50));

-- create table cars (
-- car_id serial primary key,
-- car_mark varchar (50),
-- color int REFERENCES colors (color_id) on delete no action );

-- insert into colors (name) values ('Black'), ('Green'), ('Red');
-- insert into cars (car_mark, color) values ('Audi', 1), ('Mercedes', 1), ('Tesla', 3), ('Lambou', 2);

-- delete from colors where name = 'Green'

-- set default = 'NULL'

-- Alter table cars drop constraint cars_colors_fkey;




