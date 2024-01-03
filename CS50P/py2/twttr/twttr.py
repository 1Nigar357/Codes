vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
tweet = input("Input: ")
print("Output: ", end="")
for letter in tweet:
    if letter not in vowels:
        print(letter, end="")
print()