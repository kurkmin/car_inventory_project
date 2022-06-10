DROP TABLE IF EXISTS products; 
DROP TABLE IF EXISTS manufacturers; 

CREATE TABLE manufacturers (
    name VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE products (
    name VARCHAR(255),
    description VARCHAR(255), 
    quantity INT, 
    buy_price FLOAT, 
    sell_price FLOAT,
    manufacturer_id INT REFERENCES manufacturers(id),
    id SERIAL PRIMARY KEY
); 

