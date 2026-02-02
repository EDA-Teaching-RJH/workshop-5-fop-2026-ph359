price = 75
accepted_coin = [50,20,10,5]

while price > 0:
    print(f"Price: {price}p")

    coin = int(input("Enter coins (accepted coins: 50p, 20p, 10p, 5p)"))

    if coin in accepted_coin:
        price -= coin
    else:
        print("Enter a valid coin")

print("Thank You! Dispensing Coffee")
change = abs(price)

print(f"Change: {change}p")