total = 0
acceptable_cents = [5, 10, 25, 50]
while total < 50:
    cents = int(input("Insert Coin: "))
    if cents in acceptable_cents:
        total += cents
    if total < 50:
        print(f"Amount Due: {50 - total}")
print(f"Change Owed: {total - 50}")