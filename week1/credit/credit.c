#include <cs50.h>
#include <stdio.h>

// Counter
int i = 1;

// Sum
int sum = 0;


int main(void)
{
    // Prompts the user for a number
    long number = get_long("Number: ");
    long str = number;
    do
    {
        int j = 2 * (number % 10);

        // Multiplies the digits by 2
        if (i % 2 == 0)
        {

            //Adds the digit to the sum
            sum = sum + (j % 10) + (j / 10);
            number = number / 10;
            i++;
        }

        else
        {
            sum = sum + (number % 10);
            number = number / 10;
            i++;
        }
    }

    // Checks the condition
    while (number != 0);

    // Checks if it is valid
    if (sum % 10 != 0)
    {
        printf("INVALID\n");
    }

    else
    {
        // Check if it is MasterCard or Visa
        if (str > (1e15))
        {
            if (str / (1e15) >= 4 && str / (1e15) < 5)
            {
                printf("VISA\n");
            }

            else if (str / (1e14) >= 51 && str / (1e14) < 56)
            {

                printf("MASTERCARD\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }

        // Checks if it is American Express
        else if (str > 1e14)
        {
            if (str / (1e13) >= 34 && str / (1e13) < 35)
            {
                printf("AMEX\n");
            }

            else if (str / (1e13) >= 37 && str / (1e13) < 38)
            {
                printf("AMEX\n");
            }

            else
            {
                printf("INVALID\n");
            }
        }

        //Checks if it is Visa
        else if (str > (1e12))
        {
            if (str / (1e12) >= 4  && str / (1e12) < 5)
            {
                printf("VISA\n");

            }
            else
            {
                printf("INVALID\n");
            }
        }

        else
        {
            printf("INVALID\n");

        }
    }

}