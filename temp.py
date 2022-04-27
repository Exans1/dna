import csv
import sys


def main():
    colum_count = 0
    row_count = 0
    ans = [""]
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    csvfile = sys.argv[1]
    with open(csvfile) as file:
        memory = csv.reader(file, delimiter=',')
        for row in memory:
            colum_count = len(row)
            if row_count == 0:
                index = row
            #print(row)
            row_count += 1
    print(index)
    print(colum_count)
    print(row_count)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as seq_f:
        read_seq = seq_f.read()
    # TODO: Find longest match of each STR in DNA sequence

    z = colum_count
    for y in range(1, z):
        large = 0
        j = 0
        len_index = len(index[y])
        temp = 0
        for i in range(len(read_seq)-(len_index)):
            i = j
            if i < len(read_seq) and j < len(read_seq):
                while j < len(read_seq)-len_index:
                    true = 0
                    for k in range(len_index):
                        if(index[y][k] == read_seq[j+k]):
                            true += 1
                            if true == len_index:
                                t = j + len_index
                                j = t
                                temp += 1
                            if temp > large:
                                large = temp
                    else:
                        j += 1
                        break
        ans.append(large)
    print(ans)
    # TODO: Check database for matching profiles

    return


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


import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    database = sys.argv[1]
    sequence = sys.argv[2]
    people = {}
    index = []
    keys = []

    # Saves all STRs to "shtares",
    with open(database, "r") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            index = row[1:]
            break
        # Saves all data in dictionary "people" and all keys in "keys"
        for row in reader:
            people[row[0]] = [int(x) for x in row[1:]]
            keys.append(row[0])

    print(index)
    with open(sequence, "r") as file:
        dna = file.read()

    src = []    # Samples repeat count(src)
    x = 0
    # Save number of consecutively repeated STRs for each STR
    for index in index:
        i = 0
        max_count = 0
        cur_count = 0
        index_length = len(index)
        # Check if STR matches curent DNA part
        while i <= len(dna) - index_length:
            dna_part = dna[i:i + index_length]
            if cur_count != 0:
                if dna_part != index:
                    cur_count = 0
            if dna_part == index:
                cur_count += 1
                i += index_length
            else:
                i += 1
            if cur_count > max_count:
                max_count = cur_count
        src.append(max_count)
        x += 1


    # Looking for DNA sample STRs count matches to someone's in people STRS count
    for x in range(len(keys)):
        for y in range(len(index)):
            if src == people[keys[x]]:
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
