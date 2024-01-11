print ("BPP Pizza Price Calculator\n==========================\n")

def num_pizza():
    while True:
        pizza_only = (input("Enter the number of pizzas: "))
        try:
            pizza = int(pizza_only)
            if pizza < 1:#in case the value entered by the user is less then one for example 0, -1 and so on
                print("Please enter the amount of pizza you want\n")
                continue
            else:
                break
        except ValueError:
            print("Sorry the value you entered doesnt exist!\n")
            continue

    return pizza

def delivery():
    while True:
        charge = input("do you want the pizza to be delivered? (y/n): ")
        charge = charge.lower()
        if (charge == 'y') or (charge == 'n'):
            break
        else:
            print("Please enter a valid response!\n")
            continue
    return charge

def tuesday():
    while True:
        date = input("Is today tuesday? (y/n): ")
        date= date.lower()
        if (date == 'y') or (date == 'n'):
            break
        else:
            print("Please enter a valid response!\n")
            continue
    return date

def application():
    while True:
        app_used = input("Did the customer use the app (y/n): ")
        app_used= app_used.lower()
        if (app_used == 'y') or (app_used == 'n'):
            break
        else:
            print("Please enter a valid response!\n")
            continue

    return app_used

def calculate(pizza_amount, extra_charge, special_dis, application):
    price = 12
    delivery_cost = 2.5
    pizza_sum_price= pizza_amount * price
    total_delivery_cost = 0.0
    if extra_charge and pizza_amount < :
        total_delivery_cost = DELIVERY_COST

    if special_dis == 'y' and extra_charge == 'y'  and application == 'y':
        total_price = (((pizza_sum_price - (50 / 100 * pizza_sum_price))-(25 / 100 *pizza_sum_price)) + delivery_cost)
    elif special_dis == 'y' and extra_charge == 'y' and application == 'y':
        total_price = (((pizza_sum_price - (50 / 100 * pizza_sum_price))-(25 / 100 *pizza_sum_price)) + delivery_cost)
    elif special_dis == 'n' and extra_charge == 'y' and application == 'y':
        total_price = ((pizza_sum_price -(25 / 100 *pizza_sum_price)) + delivery_cost)

    elif special_dis == 'y' and extra_charge == 'n' and application == 'y':
        total_price = ((pizza_sum_price - (50 / 100 * pizza_sum_price))-(25 / 100 *pizza_sum_price))

    elif special_dis == 'y' and extra_charge == 'y' and application == 'n':
            total_price = ((pizza_sum_price - (50 / 100 * pizza_sum_price)) + delivery_cost)

    elif special_dis == 'y' and extra_charge == 'n' and application == 'n':
        total_price = ((pizza_sum_price - (50 / 100 * pizza_sum_price)))

    elif special_dis == 'n' and extra_charge == 'y' and application == 'n':
        total_price = (pizza_sum_price + delivery_cost)

    elif special_dis == 'n' and extra_charge == 'n' and application == 'y':
        total_price = (pizza_sum_price-(25 / 100 *pizza_sum_price))



    else:
        total_price = price_of_all_pizza

    return total_price

def display(overall_cost):
    print(f"Total price: £{overall_cost:.2f}")

pizza_amount = num_pizza()
extra_charge = delivery()
special_dis = tuesday()
app_requirement = application()
overall_cost = calculate(pizza_amount, extra_charge, special_dis, app_requirement)
display(overall_cost)



