# TODO
from cs50 import get_string


def main():

    text = get_string("Text: ")

    # Count the number of letters
    letters = num_letters(text)

    # Count the number of words
    words = num_words(text)

    # Count the number of sentences
    sentences = num_sentences(text)

    """ Stores the average number of letters per
    100 words in the text in a varirable """
    L = (letters * 100) / words

    """ Stores the average number of sentences per
    100 words in the text in a varirable """
    S = (sentences * 100) / words

    # Identifies grade level using the formula
    index = 0.0588 * L - 0.296 * S - 15.8

    # Round the result gotten by the formula
    index = round(index)

    # Print the grade level
    if index > 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


# Count the number of letters in the text provided
def num_letters(text):
    i = 0
    for c in text:
        if c.isalpha() == True:
            i += 1
    return i


def num_words(text):
    # Count the number of words in the text provided
    i = 1
    for c in text:
        if c == ' ':
            i += 1
    return i


def num_sentences(text):
    # Count the number of sentences in the text provided
    i = 0
    for c in text:
        if c == '.' or c == '?' or c == '!':
            i += 1
    return i


main()