import csv
import sys


def main():
    database = sys.argv[1]
    sequence = sys.argv[2]
    people = {}
    index = []
    keys = []
    ans = []

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    with open(database, "r") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            index = row[1:]
            break

        for row in reader:
            people[row[0]] = [int(x) for x in row[1:]]
            keys.append(row[0])

    # TODO: Read DNA sequence file into a variable
    with open(sequence, "r") as file:
        dna = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    for index in index:
        bar = longest_match(dna, index)
        ans.append(bar)

    # TODO: Check database for matching profiles
    for x in range(len(keys)):
        if ans == people[keys[x]]:
            print(keys[x])
            sys.exit(0)

    print("No match")

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
