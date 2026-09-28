
# Question 1:

cups_sold = 200
# This is the Global variable

def update_sales():
    # Local variable shadowing the global variable
    cups_sold = 250

    print("Local cups sold is:", cups_sold)
    print("Global cups sold is:", globals()["cups_sold"])


update_sales()

print("Cups sold but outside function is:", cups_sold)



# Question 2:


# Daily coffee orders for five days
daily_orders = [120, 150, 180, 90, 200]

# Assigned price of one cup of coffee
cup_price = 5

# Next calculating the daily revenue using Lambda and map
daily_revenue = list(
    map(lambda cups: cups * cup_price, daily_orders)
)


high_sales = max(daily_orders)

# let's now find out the day with highest sales
best_day = daily_orders.index(high_sales) + 1

# Next trying to Display the results
print("Our daily orders:", daily_orders)
print("Our daily revenues in $:", daily_revenue)
print("Our highest daily sales:", high_sales, "cups")
print("Our best day is Day", best_day)
