// Implements a dictionary's functionality
#include <string.h>
#include <strings.h>
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

unsigned int SIZE = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = LENGTH;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int i = 0;
    node *n = NULL;
    // TODO
    do
    {
        if (i == 0)
        {
            n = table[hash(word)];
        }
        else
        {
            n = n->next;
        }
        i++;

        if (n != NULL)
        {
            int check = strcasecmp(n->word, word);
            if (check == 0)
            {
                return true;
            }
        }
    }
    while (n != NULL);

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    if (islower(word[0]))
    {
        return strlen(word) + (word[0] - 'a');
    }
    else
    {
        return strlen(word) + (word[0] - 'A');
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open Dictionary File
    FILE *ptr = fopen(dictionary, "r");
    if (ptr == NULL)
    {
        return 1;
    }

    char *word1 = malloc(sizeof(char) * (LENGTH + 1));

    // Read string from a file
    while (fscanf(ptr, "%s", word1) != EOF)
    {
        // Create a node
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            free(word1);
            return 1;
        }

        n->next = NULL;
        SIZE++;

        // Copy the srting
        strcpy(n->word, word1);

        unsigned int index = hash(word1);
        if (table[index] == NULL)
        {
            table[index] = n;
        }
        else
        {
            n->next = table[index];
            table[index] = n;
        }

    }

    // Close the file
    fclose(ptr);

    // Free
    free(word1);


    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // Returns the size of the dicitionary
    return SIZE;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Free the allocated space in the memory
    for (int i = 0; i < N; i++)
    {

        if (table[i] != NULL)
        {
            node *cursor  = table[i];
            node *tmp = table[i];
            while (cursor != NULL)
            {
                cursor = cursor->next;
                free(tmp);
                tmp = cursor;
            }
        }
    }

    return true;
}
