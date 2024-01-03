def main():
    x = get_fraction()
    if 99 <= x <= 100:
        print("F")
    elif x <= 1:
        print("E")
    else:
        print(f"{x:.0f}%")

def get_fraction():
    while True:
        fraction = input("Fraction: ")
        try:
            x , y = fraction.split("/")
            x , y = int(x), int(y)
            percent = (x / y) * 100
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if 0 <= percent <= 100:
                return percent

main()