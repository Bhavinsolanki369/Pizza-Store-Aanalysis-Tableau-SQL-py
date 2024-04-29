SELECT * FROM pizza_sales

---Q1. Total Revenue
SELECT SUM(total_price) AS total_revenue FROM pizza_sales

---Q2. Avg order value
SELECT ROUND(SUM(total_price)/COUNT(DISTINCT(order_id)),2) AS Avg_order_value  FROM pizza_sales

---Q3. Total Pizza Sold
SELECT SUM(quantity) AS Total_Pizza_Sold FROM pizza_sales

---Q4. Total Orders
SELECT COUNT(DISTINCT(order_id)) AS total_orders FROM pizza_Sales

---Q5. Avg Quantity per order
SELECT SUM(quantity)/COUNT(DISTINCT(order_id)) AS Avg_Quantity_per_order   FROM pizza_sales

---Q6. DayWise trend of orders

/* to get DAY from date in mySQL the query will be like
  SELECT DATENAME(dw, order_date) AS DayOfWeek
  FROM sales;
  but in PostgreSQL same result query is Quite different*/  
SELECT TO_CHAR(order_date,'Day') AS order_day,COUNT(DISTINCT(order_id)) AS total_orders 
FROM pizza_sales
GROUP BY order_day
ORDER BY total_orders DESC

---Q7. HourWise trend of orders
SELECT EXTRACT(Hour FROM order_time) AS Hour ,COUNT(DISTINCT(order_id)) AS total_orders FROM pizza_sales
GROUP BY EXTRACT(Hour FROM order_time)


---Q8. %age Sales by Category (Rev)
  /* Using Sub_query concept to get denominator Total revenue*/
SELECT pizza_category,
		ROUND(SUM(total_price)*100 / 
		(SELECT SUM(total_price) FROM pizza_sales),2) AS Percentage_Revenue
FROM pizza_sales
GROUP BY pizza_category


---Q9. %age Sales by Size (Rev)
SELECT pizza_size,
		ROUND(SUM(total_price)*100 / 
		(SELECT SUM(total_price) FROM pizza_sales),2) AS Percentage_Revenue
FROM pizza_sales
GROUP BY pizza_size
ORDER BY Percentage_Revenue DESC

---Q10. %age Total Pizza Sold by Category
SELECT pizza_category,SUM(quantity)*100/
		(SELECT SUM(quantity) FROM pizza_sales) AS PErcentage_Quantity
FROM pizza_sales
GROUP BY pizza_category
ORDER BY Percentage_Quantity DESC

---Q11. Top 5 Pizza by units sold
SELECT pizza_name,SUM(quantity) AS Total_Units_Sold
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Units_Sold DESC
LIMIT 5

---Q12. Bottom 5 Pizza by units sold
SELECT pizza_name,SUM(quantity) AS Total_Units_Sold
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Units_Sold ASC
LIMIT 5