#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Function that check if each letter is written only once
int diff_letters(string input);

// Function that check if all the elements in the key are letters
int all_letters(string input);


int main(int argc, string argv[])
{
    // If the user provides no command-line argument at all,
    // the program reminds the user how to use the program.
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string array = argv[1];

    // If the user doesn't provide a valid key,
    // the program explains with an error message
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    int k = all_letters(array);



    // If the user writes a non-alphabetical key,
    // the program explains with an error message
    if (k != 26)
    {
        printf("Key must only contain alphabetic characters.\n");
        return 1;
    }

    int m = diff_letters(array);

    // If the user writes more than once a letter
    // the program explains with an error message
    if (m != 0)
    {
        printf("Key must not contain repeated characters.\n");
        return 1;
    }

    // Prompt user for plaintext
    string plaintext = get_string("plaintext: ");

    // Print the word "ciphertext"
    printf("ciphertext: ");

    // Print ciphertext
    for (int n = 0, length = strlen(plaintext); n < length; n++)
    {
        int c = 0;

        if (plaintext[n] >= 'a' && plaintext[n] <=  'z')
        {
            c = plaintext[n] - 'a';
            printf("%c", tolower(array[c]));
        }

        else if (plaintext[n] >= 'A' && plaintext[n] <=  'Z')
        {
            c = plaintext[n] - 'A';
            printf("%c", toupper(array[c]));
        }
        else
        {
            printf("%c", plaintext[n]);
        }
    }

    // Moves the cursor to a new line
    printf("\n");
}












// FUNCTIONS
// Check if key inserted by the user only contains letters
int all_letters(string input)
{
    int j = 0;
    for (int i = 0, length = strlen(input); i < length; i++)
    {
        if (input[i] >= 'a' && input[i] <= 'z')
        {
            j++;
        }

        if (input[i] >= 'A' && input[i] <= 'Z')
        {
            j++;
        }
    }

    return j;
}






int diff_letters(string input)
{
    int j = 0;
    for (int i = 0, length = strlen(input); i < length; i++)
    {
        for (int v = 0; v < length; v++)
        {
            if (i != v)
            {
                if (input[i] == input[v])
                {
                    j = 1;
                    break;
                }
            }
        }
    }

    return j;
}