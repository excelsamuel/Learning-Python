# Fixed menu prices
CappuccinoPrice = 9.00
SandwichPrice = 8.50
CakePrice = 7.00

# Getting customer information
CustomerName = input("Enter your name: ")
item = input("Enter menu item (cappuccino, sandwich, or cake): ").lower()
quantity = int(input("Enter quantity: "))

# Calculate the total cost
if item == "cappuccino":
    total = CappuccinoPrice * quantity
    item_display = "cups of cappuccino"
elif item == "sandwich":
    total = SandwichPrice * quantity
    item_display = "sandwiches"
elif item == "cake":
    total = CakePrice * quantity
    item_display = "pieces of cake"
else:
    total = 0
    item_display = "unknown item"

# Display the result
if total > 0:
    print(f"Customer {CustomerName} is buying {quantity} {item_display}. "
          f"Total cost: ${total:.2f}")
else:
    print("Sorry, that menu item is not available.")
