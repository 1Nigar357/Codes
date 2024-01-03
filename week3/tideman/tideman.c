#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool winner (int a);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}











// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    int i = 0;
    do
    {
        if (!strcmp(name, candidates[i]))
        {
            ranks[rank] = i;
            return true;
        }
    i++;
    }
    while(i < candidate_count);
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    int i = 0;
    int j = 1;

    while (i < j)
    {
        preferences[ranks[i]][ranks[j]]++;

        if (j != candidate_count - 1)
        {
            j++;
        }
        else if (i < j)
        {
            i++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    int i = 0;
    int j = 0;
    int l = 0;

        do
        {
            if (i != j)
            {
                if (preferences[i][j] > preferences[j][i])
                {
                    pairs[l].winner = i;
                    pairs[l].loser = j;
                    l++;
                    pair_count++;
                }
                else if (preferences[i][j] < preferences[j][i])
                {
                    pairs[l].winner = j;
                    pairs[l].loser = i;
                    l++;
                    pair_count++;
                }
            }

            if (j < candidate_count - 1)
            {
                j++;
            }
            else if (i < j)
            {
                i++;
            }
        }
        while (i < j);

    return;
}


// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{

    if (pair_count > 0)
    {
        int counter = 1;

        while (counter != 0)
        {
            counter = 0;
                for (int i = 0; i <= pair_count - 1; i++)
                {
                    int j = i + 1;
                    if (preferences[pairs[i].winner][pairs[i].loser] < preferences[pairs[j].winner][pairs[j].loser])
                    {
                        int a = pairs[j].winner;
                        pairs[j].winner = pairs[i].winner;
                        pairs[i].winner = a;

                        int b = pairs[j].loser;
                        pairs[j].loser = pairs[i].loser;
                        pairs[i].loser = b;

                        counter++;
                    }
                }
        }
    }
    return;
}


// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{

    if (check(locked[pairs[i].winner][pairs[i].loser]))
}

// Print the winner of the election
void print_winner(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        if (winner(pairs[i].winner) == true)
        {
            printf("%s\n", candidates[pairs[i].winner]);

        }
    }
    return;
}






bool winner (int a)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (locked[i][a] == true)
        {
            return false;
        }
    }

    return true;
}