import random

def main():

    print("Welcome to CS50 GAMES!")
    print("If you want to play hangman, input 1")
    print("If you want to play guess the number game, input 2")
    while True:
        x = int(input("Which game do you want to play (1 or 2): "))
        if x == 1 or x == 2:
            break
    print()
    if x == 1:
        hangman()
    elif x == 2:
        guessNumber()


def guessNumber():
    number = random.randint(1,100)
    guess = ''
    counter = 0
    print("WELCOME TO THE GAME OF GUESS THE NUMBER")
    print("Task: Guess the secret number to win the game")
    while guess != number:
        guess = int(input("Guess a number from 1 to 100: "))
        counter += 1
        if guess == number:
            print("Congratulations! You won!!")
            print(f"Well done you guessed the number in {counter} guesses")
            break
        elif guess < number:
            print("Guess a greater number")
        else:
            print("Guess a smaller number")

    print("Do you want to play hangman?")
    print("If your answer is yes, then input 1")
    print("Otherwise, print 2")

    while True:
        a = int(input("Input: "))
        if a == 1 or a == 2:
            break
    if a == 1:
        hangman()



def hangman():
    sentence = "CS50X is the best cs course ever"
    letter = ''
    counter = 7
    guessedLetters = []
    print("WELCOME TO THE GAME OF HANGMAN!!!")
    print("Task: Guess the secret sentence to win the game")
    print("Reminder: You only have 7 guesses")
    print("You can't input the a character more than once")
    while counter != 0:
        check2 = True
        print()
        while letter in guessedLetters:
            letter = input("Input a letter or number: ")
        guessedLetters.append(letter)
        for l in sentence:
            check = False
            for letters in guessedLetters:
                if letters.lower() == l or letters.upper() == l:
                    print(l, end='')
                    check = True
            if l == ' ':
                print(' ', end='')
            elif check == False:
                print('-', end='')
                check2 = False
        print()
        if check2 == True:
            print("Congratulations! You found the secret word!")
            print()
            break
        if letter not in sentence:
            counter -= 1
            print(f"You have {counter} guess(es) left!!!")

    print("Do you want to play guess the number game?")
    print("If your answer is yes, then input 1")
    print("Otherwise, print 2")

    while True:
        a = int(input("Input: "))
        if a == 1 or a == 2:
            break
    if a == 1:
        guessNumber()


main()