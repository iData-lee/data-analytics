USE northwind; 
-- 1. Write a query to list the product id, product name, and unit price of every product that Northwind sells.
SELECT productid, productname, unitprice 
FROM products; 
-- 2. Write a query to identify the products where the unit price is $7.50 or less.
SELECT productid, productname, unitprice 
FROM products
WHERE unitprice <=7.50; 
-- 3. What are the products that we carry where we have no units on hand, but 1 or more units are on backorder?
SELECT productid, productname, unitsinstock, unitsonorder 
FROM products 
WHERE unitsinstock = 0
AND unitsinorder >= 1; 
-- 4a How does it identify the type (category) of each item sold? Answer: You can identify the type of item being sold in the CategoryID column.
SELECT productid, productname, categoryid
FROM products;
-- 4b Where can you find a list of all categories? Answer: I can find a list of all categories in the catgory table.
SELECT categoryid, categoryname
FROM categories;
-- 4c List of all the seafood items that we carry. 
SELECT productid, productname, categoryid
FROM products 
WHERE categoryid = 8; 
-- 5a  How do you know what supplier each product comes from? Answer: By the SuppliedID column
SELECT productid, productname, supplierid
FROM products; 
-- 5b Where can you find info on suppliers?  Answer: In the suppliers table. 
SELECT *
FROM suppliers; 
-- 5c Find the specific identifier for "Tokyo Traders"
SELECT supplierid, companyname
FROM suppliers
WHERE companyname = 'Tokyo Traders'; 
-- Find all products from that supplier. 
SELECT productid, productname, supplierid
FROM products 
WHERE supplierid = 4; 
-- 6a How many employees work at northwind? Answer: 9
SELECT COUNT(*) AS employee_count
FROM employees; 
-- 6b What employees have "manager" somewhere in their job title? Answer: 1, which is Steve Buchanan; who is the Sales manager.
SELECT employeeid, firstname, lastname, title
FROM employees
WHERE title LIKE '%manager%';