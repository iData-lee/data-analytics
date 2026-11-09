/* The name of the table that shows what northwind sells is the product table. 
 The table that holds the type/categories of items sold is the Categories table*/
SELECT * FROM employees;
-- Peacock, Margaret is the employee who's name makes it sound as if she is a bird. 
SELECT * FROM products; 
/* A total of 77 records appear. 
You can change the retrieval of 10 rows in the toolbar dropdown with the Limit of 1000 rows. 
*/
SELECT * FROM categories; 
# The category code for seafood is 8. 
SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders 
LIMIT 50;
