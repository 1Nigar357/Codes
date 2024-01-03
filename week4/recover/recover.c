#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

typedef uint8_t BYTE;
const int BLOCK_SIZE = 512;
int counter = 0;

int arr[] = {0xff, 0xd8, 0xff};
uint8_t data[BLOCK_SIZE];

// Function that checks if a new JPEG file is found
int check_if_JPEG(uint8_t arr1[], int arr2[]);

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc < 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *new = NULL;

    // Open files and determine scaling factor
    FILE *f = fopen(argv[1], "r");
    if (f == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // New filename
    char filename[8];
    while (fread(data, sizeof(uint8_t), BLOCK_SIZE, f) == BLOCK_SIZE)
    {
        int check = check_if_JPEG(data, arr);

        // If a JPEG file is found
        if (check == 0)
        {
            // Create a new JPEG file
            sprintf(filename, "%03i.jpg", counter);

            // Open the new file
            new = fopen(filename, "w");
            if (new == NULL)
            {
                printf("Could not open file.\n");
                return 1;
            }

            // Increment counter
            counter++;
        }

        // If a JPEG file was already found before
        if (counter > 0)
        {

            // Recover the image by writing the JPEG file data to a new file
            fwrite(data, sizeof(uint8_t), BLOCK_SIZE, new);
        }
    }
}








int check_if_JPEG(uint8_t arr1[], int arr2[])
{
    for (int i = 0; i < 3; i++)
    {
        if (data[i] != arr[i])
        {
            return 1;
        }
    }

    if ((data[3] & 0xf0) != 0xe0)
    {
        return 1;
    }

    return 0;
}
