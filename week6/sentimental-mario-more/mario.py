# TODO
from cs50 import get_int


def main():
    height = get_height()

    # Print the 2 half pyramids
    for j in range(1, height + 1):
        space = height - j

        # Indent
        print(" " * space, end='')

        # Print the '#' symbols
        print("#" * j, end='')

        # Print the gap between the 2 half pyramids
        print(" " * 2, end='')

        # Print the '#' symbols
        print("#" * j)


# Gets the height from the user
def get_height():
    while True:
        height = get_int("Size: ")
        if height >= 1 and height <= 8:
            break
        else:
            print("Write a number between 1 and 8")
    return height


main()