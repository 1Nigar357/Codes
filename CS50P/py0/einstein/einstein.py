def main():
    m = int(input("m: "))
    E = formula(m)
    print(f"E: {E}")

def formula(x):
    return x * pow (300000000, 2)

main()