Km = int(input("enter the kilometer to drive: "))
liters =int(input("enter the liters per kilometer: "))
price = int(input("enter the price per liter: "))

def cal_cost(Km,liters,price):
    total_liters = Km * liters
    total_cost = total_liters * price
    return total_cost

trip_cost = cal_cost(Km, liters, price)
print(f"The cost of the trip is: ₹{trip_cost}")

