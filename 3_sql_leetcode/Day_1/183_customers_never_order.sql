183. Customers Who Never Order
https://leetcode.com/problems/customers-who-never-order/
----------------------------------------------------------

Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

🐳----------------🐳----------------🐳----------------🐳----------------🐳----------------🐳----------------
# Write your MySQL query statement below
SELECT
    t.Name AS Customers
FROM (
    SELECT o.Id AS orderId
          , c.Name AS Name
    FROM Customers AS c
    LEFT JOIN Orders AS o
    ON c.Id = o.CustomerId
) t
WHERE t.orderID is null
ORDER BY t.Name


🐳----------------
SELECT NAME AS Customers
FROM CUSTOMERS
WHERE ID NOT IN (SELECT CUSTOMERID FROM ORDERS)
