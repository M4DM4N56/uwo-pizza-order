# import pizzaReceipt
from pizzaReceipt import generateReceipt
# topping constant
TOPPINGS = ("ONION", "SPINACH", "HAM", "TOMATO", "BROCCOLI", "BACON", "GREEN PEPPER", "PINEAPPLE",
            "GROUND BEEF", "MUSHROOM", "HOT PEPPER", "CHICKEN", "OLIVE", "PEPPERONI", "SAUSAGE")

# initializing pizza list and first prompt
pizza_list = []
prompt = input("Do you want to order pizza? Enter [NO] or [QUIT] to decline:   ")
prompt = prompt.upper()
looping = True

if prompt != "NO" and prompt != "Q":
    while looping:

        # size selection + foolproof-ing
        size = input("\nChoose a size:")
        size = size.upper()
        while size != "S" and size != "M" and size != "L" and size != "XL":
            size = input("\nChoose a size:")
            size = size.upper()

        # initialize topping list
        pizza_toppings = []
        topping_finish = False

        # prompt topping loop
        while topping_finish is False:
            topping_pick = input("Type in one of our toppings to add it to your pizza. To see the list of toppings, enter \"LIST\". When you are done adding toppings, enter \"X\"\n")
            topping_pick = topping_pick.upper()

            # possible outputs
            if topping_pick == "LIST":
                print(TOPPINGS)
            elif topping_pick == "X":
                topping_finish = True
            elif topping_pick in TOPPINGS:
                pizza_toppings.append(topping_pick)
                print("You have added " + topping_pick + " to your pizza")

        # organizes pizza and put it into a list of pizzas
        pizza = (size, pizza_toppings)
        pizza_list.append(pizza)

        # loop again?
        prompt = input("Do you want to order pizza? Enter [NO] or [QUIT] to decline:   ")
        prompt = prompt.upper()
        if prompt == "NO" or prompt == "Q":
            looping = False

else:
    print("You did not order anything")

# go to next file
generateReceipt(pizza_list)
