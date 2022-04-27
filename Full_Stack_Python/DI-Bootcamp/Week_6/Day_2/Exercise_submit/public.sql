-- select * from items order by price desc;
-- select * from items where price > 80 order by price desc;

-- CREATE TEMPORARY TABLE TempCustomers AS SELECT * FROM customers;
-- ALTER TABLE TempCustomers DROP COLUMN customer_id;
-- select * from TempCustomers fetch first 3 rows only;

-- CREATE TEMPORARY TABLE TempCustomers2 AS SELECT * FROM customers;
-- ALTER TABLE TempCustomers2 DROP COLUMN customer_id;
-- ALTER TABLE TempCustomers2 DROP COLUMN first_name;
-- select * from TempCustomers2 order by last_name desc;

-- CREATE TABLE purchases (
-- 	purchase_id SERIAL PRIMARY KEY,
-- 	customer_id INTEGER,
-- 	item_id INTEGER, 
-- 	quantity_purchased integer,
-- 	FOREIGN KEY (customer_id) REFERENCES customers (customer_id), 
-- 	FOREIGN KEY (item_id) REFERENCES items (item_id));
	
-- insert into purchases (customer_id, item_id, quantity_purchased ) 
-- values (
-- (select customer_id from customers where first_name = 'Scott' AND last_name = 'Scott'),
-- (select item_id from items where item_name = 'Fan'), (1));

-- select customer_id from customers where first_name = 'Scott' AND last_name = 'Scott', select item_id from items where item_name = 'Fan', '1'));

-- select item_id from items where item_name = 'Fan';
-- select customer_id from customers where first_name = 'Scott' AND last_name = 'Scott'

-- select * from purchases

-- insert into purchases (customer_id, item_id, quantity_purchased) 
-- values (
-- (select customer_id from customers where first_name = 'Melanie' AND last_name = 'Johnson'),
-- (select item_id from items where item_name = 'Large desk'), (10));
	
-- insert into purchases (customer_id, item_id, quantity_purchased) 
-- values (
-- (select customer_id from customers where first_name = 'Greg' AND last_name = 'Jones'),
-- (select item_id from items where item_name = 'Small Desk'), (2));

-- select * from purchases

Select customers.customer_id ,customers.first_name, customers.last_name, purchases.quantity_purchased
from customers inner join purchases on customers.customer_id = purchases.customer_id;




