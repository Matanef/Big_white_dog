-- select * from students;
-- select first_name, last_name from students;
-- select first_name, last_name from students where student_id = 2;
-- select first_name, last_name from students where last_name = 'Benichou' and first_name = 'Marc';
-- select first_name, last_name from students where last_name = 'Benichou' or first_name = 'Marc'
-- select first_name, last_name from students where first_name like '%A%'
-- select first_name, last_name from students where first_name like '%a';
-- select first_name, last_name from students where first_name like 'A%';
select first_name, last_name from students where first_name like '%-2'