#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Declare r, g, b, shade variables
    float r, g, b;
    int shade;

    // Iterate through each row
    for (int i = 0; i < height; i++)
    {
        // Iterate through each pixel in a row
        for (int j = 0; j < width; j++)
        {
            r = image[i][j].rgbtRed;
            g = image[i][j].rgbtGreen;
            b = image[i][j].rgbtBlue;

            /*
                If all the values are equal
                no need to calculate the average value -
                it is already done fo you
            */
            if (r == g && r == b)
            {
                shade = r;
            }
            else
            {
                // Calculate the average
                shade = round((r + g + b) / 3);
            }

            // Assign the new RGB values to a pixel
            image[i][j].rgbtRed = shade;
            image[i][j].rgbtGreen = shade;
            image[i][j].rgbtBlue = shade;

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Declare r, g, b variables
    int r, b, g;

    // Declare and intialize the middle variable
    int middle = width / 2;

    for (int i = 0; i < height; i++)
    {
        // Declare and initialize the counter j
        int j = 0;

        // Loop until you reach the middle
        while (j < middle)
        {
            // Swap the RGB values of two pixels
            r = image[i][width - (1 + j)].rgbtRed;
            b = image[i][width - (1 + j)].rgbtBlue;
            g = image[i][width - (1 + j)].rgbtGreen;

            image[i][width - (1 + j)].rgbtRed = image[i][j].rgbtRed;
            image[i][width - (1 + j)].rgbtBlue = image[i][j].rgbtBlue;
            image[i][width - (1 + j)].rgbtGreen = image[i][j].rgbtGreen;

            image[i][j].rgbtRed = r;
            image[i][j].rgbtBlue = b;
            image[i][j].rgbtGreen = g;

            // Increment the counter
            j++;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    // Create an array that will store the new RGB values of each pixel
    RGBTRIPLE image2[height][width];
    //iterate through each row
    for (int i = 0; i < height; i++)
    {
        //iterate through each pixel in a row
        for (int j = 0; j < width; j++)
        {
            //set counter and RGB values' variables
            float r = 0;
            float g = 0;
            float b = 0;
            int counter = 0;

            /*
                calculate the average of each color
                by adding the RGB values of each pixel around
                the center pixel amd of the center pixel itself
            */
            for (int n = -1; n < 2; n++)
            {
                for (int m = -1; m < 2; m++)
                {
                    int k = i + n;
                    int l = j + m;

                    // Check if a pixel is past the boundaries of an image
                    if (l > -1 && l < width && k > -1 && k < height)
                    {
                        r += image[k][l].rgbtRed;
                        g += image[k][l].rgbtGreen;
                        b += image[k][l].rgbtBlue;
                        counter++;
                    }
                }
            }
            // Store the new RGB values in the image2 array
            image2[i][j].rgbtRed = round(r / counter);
            image2[i][j].rgbtGreen = round(g / counter);
            image2[i][j].rgbtBlue = round(b / counter);
        }
    }

    // Assign the new RGB values to each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = image2[i][j].rgbtRed;
            image[i][j].rgbtGreen = image2[i][j].rgbtGreen;
            image[i][j].rgbtBlue = image2[i][j].rgbtBlue;
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{

    // Set arrays for later usage in matrix calculations
    int arrx[] = {-1, 0, 1, -2, 0, 2, -1, 0, 1};
    int arry[] = {-1, -2, -1, 0, 0, 0, 1, 2, 1};

    // Create an array that will store the new RGB values of each pixel
    RGBTRIPLE image2[height][width];

    // Iterate through each row
    for (int i = 0; i < height; i++)
    {
        // Iterate through each pixel in a row
        for (int j = 0; j < width; j++)
        {
            // Set counter and RGB values' variables
            int GXr = 0, GXg = 0, GXb = 0;
            int GYr  = 0, GYg = 0, GYb = 0;
            int counter = 0;
            int z = 0;


            // Iterate through each row around the center pixel
            for (int n = -1; n < 2; n++)
            {
                // Iterate through each pixel in each row around the center pixel
                for (int m = -1; m < 2; m++)
                {
                    int k = i + n;
                    int l = j + m;

                    // Check if a pixel is past the boundaries of an image
                    if (l > -1 && l < width && k > -1 && k < height)
                    {
                        // Matrix
                        GXr += image[k][l].rgbtRed * arrx [z];
                        GXg += image[k][l].rgbtGreen  * arrx [z];
                        GXb += image[k][l].rgbtBlue  * arrx [z];

                        GYr += image[k][l].rgbtRed * arry [z];
                        GYg += image[k][l].rgbtGreen  * arry [z];
                        GYb += image[k][l].rgbtBlue  * arry [z];
                        counter++;
                    }
                    z++;
                }
            }

            // Calculate the RGB values
            int r = round(sqrt(pow(GXr, 2) + pow(GYr, 2)));
            int g =  round(sqrt(pow(GXg, 2) + pow(GYg, 2)));
            int b = round(sqrt(pow(GXb, 2) + pow(GYb, 2)));

            // If the value is more than 255 assign the RGB value of 255
            if (r > 255)
            {
                r = 255;
            }

            if (g > 255)
            {
                g = 255;
            }

            if (b > 255)
            {
                b = 255;
            }

            // Store new RGB values in the image2 array
            image2[i][j].rgbtRed = r;
            image2[i][j].rgbtGreen = g;
            image2[i][j].rgbtBlue = b;
        }
    }

    // Assign the new RGB values to each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = image2[i][j].rgbtRed;
            image[i][j].rgbtGreen = image2[i][j].rgbtGreen;
            image[i][j].rgbtBlue = image2[i][j].rgbtBlue;
        }
    }
    return;
}
