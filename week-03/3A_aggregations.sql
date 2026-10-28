USE northwind; 
-- 1 Find the price of the cheapest item that Northwind sells. 
SELECT MIN(unitprice)
FROM products; 
-- 1a Find the name of the product that has that price. 
Select productname, unitprice 
FROM products 
WHERE unitprice = 2.50;
--  2 Find the average price of all items that Northwind sells * bonus ROUND AVG 
SELECT ROUND(AVG(unitprice), 2)
FROM products; 
--  3 Find the price of the most expensive item that Northwind sells. 
SELECT MAX(unitprice)
FROM products; 
-- 3a Find the name of the product with that price, plus the name of the supplier for that product 
SELECT p.productname, p.unitprice, s.companyname
FROM products p 
JOIN suppliers s ON p.supplierid = s.supplierid
WHERE p.unitprice = 263.50; 
-- 4 Find total monthly payroll (the sum of all the employees’ monthly salaries) 
SELECT SUM(salary)
FROM employees; 
-- 5 Identify the highest salary and the lowest salary amounts which any employee makes.
-- (Just the amounts, not the specific employees!)
SELECT MAX(salary), MIN(salary) 
FROM employees; 
-- 6 Find the name and supplier ID of each supplier and the number of items they supply. 
-- Hint: Join is your friend here. 
SELECT s.companyname, s.supplierid, COUNT(p.productid)
FROM suppliers s
JOIN products p ON p.supplierid = s.supplierid 
GROUP BY s.supplierid, s.companyname; 
-- 7 Find the list of all category names and the average price for items in each category. 
SELECT c.categoryname, AVG(p.unitprice) 
FROM categories c 
JOIN products p ON c.categoryid = p.categoryid 
GROUP BY c.categoryid, c.categoryname; 
-- 8 Find, for all suppliers that provide at least 5 items to Northwind, 
-- what is the name of each supplier and the number of items they supply. 
SELECT s.companyname, COUNT(p.productid)
FROM suppliers s 
JOIN products p ON s.supplierid = p.supplierid 
GROUP BY s.supplierid, s.companyname
HAVING COUNT(p.productid) >= 5; 
-- 9 List products currently in inventory by the product id, product name, and inventory value  
-- (calculated by multiplying unit price by the number of units on hand). 
-- Sort the results in descending order by value. If two or more have the same value, order by product name. 
--  If a product is not in stock, leave it off the list. 
SELECT productid, productname, unitprice * unitsinstock AS inventoryvalue
FROM products  
WHERE unitsinstock > 0 
ORDER BY inventoryvalue DESC, productname;