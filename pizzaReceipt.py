# initializing price record list for the receipt + total
pizza_record = []
topping_record = []
topping_prices = []
total_cost = 0


def calculate_price(pizza_order):
    global total_cost
    # for amount of pizzas ordered
    for i in range(len(pizza_order)):
        pizza_price = 0.00
        topping_price = 0.00
        # size determines price of base pizza
        if pizza_order[i][0] == "S":
            pizza_price += 7.99
            topping_charge = 0.50
        elif pizza_order[i][0] == "M":
            pizza_price += 9.99
            topping_charge = 0.75
        elif pizza_order[i][0] == "L":
            pizza_price += 11.99
            topping_charge = 1.00
        elif pizza_order[i][0] == "XL":
            pizza_price += 13.99
            topping_charge = 1.25
        # this should be redundant, but I would get an error if I didn't initialize topping_charge...
        else:
            topping_charge = 0
            print("You did not order anything")

        # calculates & checks to see if we need to charge extra for toppings
        topping_num = len(pizza_order[i][1])
        if topping_num > 3:
            topping_num = topping_num - 3
            topping_price = topping_price + (topping_num * topping_charge)

        # organizing everything in nice lists to be called for the receipt
        topping_record.append(topping_price)
        pizza_record.append(pizza_price)
        total_cost += (pizza_price + topping_price)
        topping_prices.append(topping_charge)


def generateReceipt(pizza_order):
    # calculate prices before receipt is printed
    calculate_price(pizza_order)

    # if pizzas have been ordered, print receipt
    if len(pizza_order) > 0:
        print("Your order:")

        # prints pizza number, size, and base price
        for c in range(len(pizza_order)):
            print("Pizza " + str(c+1) + ": " + pizza_order[c][0] + " 				  " + '{0:.2f}'.format(pizza_record[c]))

            # prints toppings one by one
            for t in range(len(pizza_order[c][1])):
                print("- " + pizza_order[c][1][t])

            # prints the extra topping fees (if any)
            if topping_record[c] > 0:
                counter = 0
                while counter != topping_record[c]:
                    size = pizza_order[c][0]
                    print("Extra Topping (" + size + ")		   " + '{0:.2f}'.format(topping_prices[c]))
                    counter += topping_prices[c]

        # calculates and prints the final cost and tax
        tax = total_cost * 0.13
        print("Tax:					   {0:.2f}".format(tax))
        final_total = tax + total_cost
        print("Total:					  {0:.2f}".format(final_total))

    else:
        print("You did not order anything")
