# Simple Cafe Ordering System
menu = {
    "coffee": 50, 
    "tea": 30,
    "sandwich": 80,
    "cake": 60,
    "pasta": 100,
    "juice": 40,
    "pizza": 120,
    "burger": 90,
    "rolls": 70,
    "salad": 60
}

print("Welcome to the Cafe!")
print("Menu:")
print("Coffee - $50\nTea - $30\nSandwich - $80\nCake - $60\nPasta - $100\nJuice - $40\nPizza - $120\nBurger - $90\nRolls - $70\nSalad - $60")

order_total = 0

item_1 = input("Enter the first item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order. Current total: ${order_total}")
else:
    print(f"Sorry, {item_1} is not on the menu.")

another_item = input("Do you want to order another item? (yes/no): ")
if another_item == "yes":
    item_2 = input("Enter the second item you want to order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} added to your order. Current total: ${order_total}")
    else:
        print(f"Sorry, {item_2} is not on the menu.")
else:
    print(f"Your final order total is: ${order_total}")
