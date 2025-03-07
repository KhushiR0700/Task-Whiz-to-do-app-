menu = {
    'Pizza': 150,
    'Lava cake' : 120,
    'chicken wrap': 156,
    'Chicken wings' : 250,
    'Brew' : 546,
    'Pancakes' : 434,
    'Coffee': 89,
}

print("Welcome to Royal Relish Restaurant")
print("Pizza: Rs150\nLava cake: Rs120\nchicken wrap: Rs156\nChicken wings: Rs250\nBrew: Rs546\nPancakes:Rs434\nCoffee:89")

order_total = 0

item_1 = input("enter the name of item you want to order = ").strip().title()
if item_1 in menu:
    order_total +=menu[item_1] 
    print(f"Your item {item_1} has been added to your order!")

else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (Yes/No)").strip().title()  
if another_order == "Yes":
    item_2 = input("enter the name of second item =").strip().title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order") 
    else:
        print(f"Ordered item {item_2} is not available yet!")

print(f"The total amount of items to pay is {order_total}")
