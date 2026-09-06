CREATE TABLE users (
    id INT PRIMARY KEY,
    nom VARCHAR(50),
    ville VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    produit VARCHAR(50),
    montant DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users (id, nom, ville) VALUES 
(1, 'Alice', 'Paris'),
(2, 'Bob', 'Lyon'),
(3, 'Charlie', 'Marseille');

INSERT INTO orders (order_id, user_id, produit, montant) VALUES 
(101, 1, 'Clavier', 45.00),
(102, 1, 'Souris', 25.50),
(103, 2, 'Ecran', 199.99); 

SELECT * FROM orders;

SELECT produit
FROM orders
WHERE montant > 40;

SELECT order_id 
FROM orders
ORDER BY montant DESC;

SELECT COUNT(order_id)
FROM orders;

SELECT order_id, nom, produit, montant
FROM users JOIN orders ON users.id = orders.user_id;

SELECT order_id 
FROM orders 
WHERE montant <= 45.00;

SELECT nom 
FROM users
ORDER BY nom DESC;

SELECT COUNT(ville)
FROM users
WHERE ville LIKE 'Paris';

SELECT nom, produit 
FROM users JOIN orders ON users.id = orders.user_id
WHERE montant > 30;

SELECT * 
FROM users JOIN orders ON users.id = orders.user_id
WHERE nom LIKE 'Alice';