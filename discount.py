# Function to calculate total expenses with discount
def calculate_total_expense(quantity, price_per_item):
    total_cost = quantity * price_per_item
    if quantity > 10:
        discount = total_cost * 0.10  
        total_cost -= discount
    return total_cost


quantity = int(input("Enter the quantity of items purchased: "))
price_per_item = float(input("Enter the price per item: "))

total_expenses = calculate_total_expense(quantity, price_per_item)
print(f"The total expenses are: ₹{total_expenses}")
