cost = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

def main():
    total = 0
    while True:
        x = order()
        if x == 1:
            break
        total += x
        print(f"Total: ${total:.2f}")

def order():
    while True:
        try:
            food = input("Item: ").title()
            price = cost[food]
        except EOFError:
            print()
            exit()
        except KeyError:
            pass
        else:
            return price

main()