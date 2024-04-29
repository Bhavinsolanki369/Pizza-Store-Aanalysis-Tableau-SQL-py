import numpy as np
import pandas as pd
import datetime as dt



pizza = pd.read_csv(r'D:\Business Analyst\projects\pizza_sales.csv')
#print(pizza.head())
#print(pizza.info())
total_revenue = pizza['total_price'].sum()
total_orders =pizza['order_id'].nunique()
total_units = pizza['quantity'].sum()


#   Q1. Total Revenue
total_revenue = pizza['total_price'].sum()
print("Total Revenue is " + str(total_revenue) + ' USD.')

#   Q2. Avg order value
print("Average order value is " + str(round(total_revenue/total_orders,2)) + ' USD.')

#   Q3. Total Pizza Sold
print("Total units of pizzas sold is " + str(total_units) + ' Pizza.')

#   Q4. Total Orders
print("Total number of orders completed is "+ str(total_orders) + ' Orders.')

#   Q.5 What is Average Quantity per order?
print("Average quantity per order is " + str(round(total_units/total_orders,2)) + ' Pizza.')

#   Q6. DayWise trend of orders
''' our DF(pizza) have date clm. We wanted Day to answer this question. therefore
G---[pd.to_datetime() One more important learning, i got an error on date 13-01-2015
i could understand that, this error was because of
date format("%m-%d-%Y") which is by default
recognising this i changed it to ,format="%d-%m-%Y" and it worked.
after  that i have imported DATETIME as dt and used .day_name() to name day of week'''

pizza['order_date'] = pd.to_datetime(pizza['order_date'],format="%d-%m-%Y")
pizza['day'] = pizza['order_date'].dt.day_name()
dayWise_orders = pizza.groupby('day').nunique()['order_id'].sort_values(ascending=False)
print(
)
print('Days Wise trend in orders.')
print(dayWise_orders)

#   Q7. HourWise trend of orders
'''i could not find correct method. but i tried to manipulate
order_time clm to get hours. to extract hours i asked to get first
2 CHAR. consideriing value as string.'''

pizza['order_time'] = pizza['order_time'].str[:2]
print(
)
print("Hour wise trend of orders Suggesting peak and low hours.")
print(pizza.groupby('order_time').nunique()['order_id'])

#   Q8. %age Revenue by Category
cat_rev = pizza.groupby('pizza_category').sum('total_price')['total_price']
print(
)
print("Percentage Revenue by pizza Category.")
print(round(cat_rev*100/total_revenue,2))

#   Q9. %age Revenue by Size
size_rev = pizza.groupby('pizza_size').sum('total_price')['total_price']
print(
)
print("Percentage Revenue by pizza Size.")
print(round(size_rev*100/total_revenue,2))

#   Q10. %age Total Pizza Sold(units) by Category
cat_sale_count = pizza.groupby('pizza_category').sum('quantity')['quantity']
print(
)
print("Percentage of total number of pizzas sold by Category.")
print(round(cat_sale_count*100/total_units,2))

#   Q11. Top 5 Pizza by units sold
'''PN sales_name here is a SERIES there for .sort_values(ascending=False/True)
have this argument, because series dont have columns
whereas, for DF we have .sort_values(by=) here we provide column by which to sort
.head() is used to get TOP VALUES, 5 is by default how ever you can provide number.
eg,    .head(10)'''
sale_name = pizza.groupby('pizza_name').sum('quantity')['quantity']
print(
)
print("Top 5 most popular pizza (based on units sold).")
print(sale_name.sort_values(ascending=False).head())

#   Q12. Bottom 5 Pizza by units sold
'''PN sales_name here is a SERIES there for .sort_values(ascending=False/True)
have this argument, because series dont have columns
whereas, for DF we have .sort_values(by=) here we provide column by which to sort
.head() is used to get TOP VALUES, 5 is by default how ever you can provide number.
eg,    .head(10)'''
sale_name = pizza.groupby('pizza_name').sum('quantity')['quantity']
print(
)
print("Bottom 5 most popular pizza (based on units sold).")
print(sale_name.sort_values().head())









