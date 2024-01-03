import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) < 3:
        print("Usage: python dna.py data.csv sequence.txt")
        return 1

    # TODO: Read database file into a variable
    people = []

    database = sys.argv[1]
    with open(database, "r") as data:
        reader = csv.DictReader(data)
        for row in reader:
            people.append(row)

    # TODO: Read DNA sequence file into a variable
    dna = sys.argv[2]
    with open(dna, "r") as f:
        string = f.readline()

    # Find longest match of each STR in DNA sequence
    with open(database, "r") as data:
        reader = csv.reader(data)
        row = next(reader)
        dnas = row

    for i in range(1, len(dnas)):
        subsequence = dnas[i]

        check = longest_match(string, subsequence)

        # TODO: Check database for matching profiles
        index = []
        for i in range(len(people)):
            if int(people[i][subsequence]) != check:
                index.append(i)

        counter = 0
        for i in range(len(index)):
            j = index[i] - counter
            del people[j]
            counter += 1

    # Print the person's name
    try:
        print(people[0]['name'])
    except:
        print("No match")
    return 0


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
