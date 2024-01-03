#include <cs50.h>
#include <math.h>
#include <string.h>
#include <stdio.h>

// Function that counts the letters in a text
int count_letters(string text);

// Function that counts the words in a text
int count_words(string text);

// Function that counts the sentences in a text
int count_sentences(string text);

int main(void)
{
    // Prompt user for a string
    string text = get_string("Text: ");

    // Store the number of letters, words, and sentences in the text in three variables
    float letters = count_letters(text);
    float words = count_words(text);
    float sentences = count_sentences(text);

    // Stores the average number of letters per 100 words in the text in a varirable
    float L = (letters * 100) / words;

    // Stores the average number of sentences per 100 words in the text in a varirable
    float S = (sentences * 100) / words ;

    // Identifies the grade level by using the formula
    float f = 0.0588 * L - 0.296 * S - 15.8;

    // Rounds the result
    int index = round(f);

    // Prints the grade level
    if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }

}





int count_letters(string text)
{
    int j = 0;
    for (int i = 0, length = strlen(text); i < length; i++)
    {
        if (text[i] >= 'a' && text[i] <= 'z')
        {
            j++;
        }
        if (text[i] >= 'A' && text[i] <= 'Z')
        {
            j++;
        }
    }

    return j;
}

int count_words(string text)
{
    int j = 0;
    for (int i = 0, length = strlen(text); i < length; i++)
    {

        if (text[i] == ' ')
        {
            j++;
        }
    }
    j++;
    return j;
}

int count_sentences(string text)
{
    int j = 0;
    for (int i = 0, length = strlen(text); i < length; i++)
    {

        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            j++;
        }
    }

    return j;
}
