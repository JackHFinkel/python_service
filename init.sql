create table IF NOT EXISTS items (id serial PRIMARY KEY, name varchar, price integer);
insert into items(name,price) values ('chair',100);