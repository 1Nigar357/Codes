def main():
    variable = input("camelCase: ")
    snake_case(variable)

def snake_case(word):
    print("snake_case: ", end='')
    for letter in word:
        if letter.isupper():
            letter = letter.lower()
            print(f"_{letter}", end='')
        else:
            print(letter, end='')
    print()


main()
