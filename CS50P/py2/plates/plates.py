def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[0:2].isalpha():
        return False
    i = 0
    for letter in s:
        if not letter.isdigit() and not letter.isalpha():
            return False
        if letter.isdigit():
            if i == 0 and letter == '0':
                return False
            i += 1
        if i != 0 and letter.isalpha():
            return False

    return True



main()