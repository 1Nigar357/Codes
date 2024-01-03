# TODO
from cs50 import get_int

number = get_int("Number: ")
# Make a copy of the number inputed by the user
copy = number

# Convert the integer to a string
string = str(number)

# Count the number of digits in the integer
length = len(string)


def main():
    # Check if the card number is valid
    sum = is_valid(string, copy)

    # If sum isn't diviible by 10, then print "INVALID"
    if sum % 10 != 0:
        print("INVALID")

    # Check if it is VISA
    if length == 13 or length == 16:
        quotient = int(number / 10 ** (length - 1))
        if quotient == 4:
            print("VISA")
            return 0
    # Check if it is American Express
    elif length == 15:
        quotient = int(number / 10 ** (length - 2))
        if quotient == 34 or quotient == 37:
            print("AMEX")
            return 0
    # Check if it is Master Card
    if length == 16:
        quotient = int(number / 10 ** (length - 2))
        if quotient >= 51 and quotient <= 55:
            print("MASTERCARD")
            return 0
    # If none of the above is true, then print "INVALID"
    else:
        print("INVALID")


# Checks if the card number is valid
def is_valid(string, copy):
    sum = 0
    for i in range(len(string)):
        # Assigns
        if i % 2 == 0:
            i = copy % 10
        else:
            i = 2 * (copy % 10)
            if i > 9:
                i = int(i % 10) + int(i / 10)
        sum += i
        copy = int(copy / 10)
    return sum


main()