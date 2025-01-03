
# Define the items and prices
items = ['bread', 'cookies', 'butter', 'cheese', 'yoghurt']
prices = [40, 80, 120, 180, 60]
cart = []
print(items)
while True:
    print("\nEnter 1 for viewing the items")
    print("Enter 2 for adding the items in cart")
    print("Enter 3 for updating the items in cart")
    print("Enter 4 for deleting the items in cart")
    print("Enter 5 for printing bill")
    print("Enter 6 to exit")
    
    choice = int(input("Enter your choice: "))
    '''View'''
    if choice == 1:
        print("\nAvailable items:")
        for i in range(len(items)):
            print(f"Name: {items[i]} Price: {prices[i]}")
    
    elif choice == 2:#add
        item_name = input("Enter the Name of item: ")
        if item_name in items:
            quantity = int(input("Enter the quantity: "))
            item_index = items.index(item_name)
            cart.append([item_name, quantity, prices[item_index], prices[item_index] * quantity])
        else:
            print("Item not available!")
            
    
    elif choice == 3:#update
        item_name = input("Which item to be updated: ")
        for i in range(len(cart)):
            if cart[i][0] == item_name:
                new_quantity = int(input(f"Enter the new quantity for {item_name}: "))
                cart[i][1] = new_quantity
                cart[i][3] = cart[i][1] * cart[i][2]  # Update total price for the item
                print(f"Updated {item_name} quantity to {new_quantity}.")
                break
        else:
            print(f"Item {item_name} not found in the cart!")
            
   
    elif choice == 4:#delete
        item_name = input("Which item to be removed: ")
        for i in range(len(cart)):
            if cart[i][0] == item_name:
                cart.pop(i)
                print(f"Removed {item_name} from the cart.")
                break
        else:
            print(f"Item {item_name} not found in the cart!")
            
    
    elif choice == 5:
        if cart:
            print("\nName, Quantity, Price, Total")
            total_amount = 0
            for item in cart:
                print(f"{item[0]},{item[1]},{item[2]},{item[3]}")
                total_amount += item[3]
            print(f"\nTotal Amount of Bill: {total_amount}")
        else:
            print("Your cart is empty!")
            
   
    elif choice == 6:
        print("Exiting... Thank you for shopping!")
        break

    else:
        print("Invalid choice! Please try again.")
