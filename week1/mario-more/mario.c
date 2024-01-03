//Week 1
// Code Mario
#include <cs50.h>
#include <stdio.h>


int height;
int row = 0;

int main(void)
{
    while (true)
    {
        height = get_int("Height: ");
        if (height >= 1 && height <= 8)
        {

            break;
        }
    }
    int k = height;
    do
    {

        row++;
        k--;
        int i = 0;

        //puts space
        int subtraction = height - row;

        while (i < subtraction)
        {
            printf(" ");
            i++;
        }

        //prints "#" sign
        for (int j = 0; j < height - i; j++)
        {
            printf("#");
        }

        printf("  ");

        for (int j = 0; j < height - i; j++)

            printf("#");
        }

        printf("\n");

    }

    while (k >= 1);

}

