# use grocery_store;-- 

# show databases;

# select * from products;

# select * from uom;
/*
INSERT INTO orders (order_id, customer_name, total, datetime)
VALUES (1, 'Arav', 250.75, '2025-04-30 10:45:00');
*/

# select * from orders;

-- SELECT products.prouct_id, products.name, products.uom_id,
-- products.price_per_unit FROM products INNER JOIN uom on uom.uom_id = products.uom_id;

SELECT p.product_id, p.name, p.price_per_unit, u.uom_id, u.uom_name
    FROM products p
    INNER JOIN uom u ON p.uom_id = u.uom_id;


INSERT INTO products (name, uom_id, price_per_unit) VALUES ("face mask", 1, 20);

select * from products;


