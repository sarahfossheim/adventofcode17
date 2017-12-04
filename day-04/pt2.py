# --- Part Two ---
#
# For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.
#
# For example:
#
# abcde fghij is a valid passphrase.
# abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
# a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
# iiii oiii ooii oooi oooo is valid.
# oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
# Under this new system policy, how many passphrases are valid?

import csv

# Count the lines with only unique words
count = 0

# Get the passphrase from the input file
with open('pt2.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    # Loop through the rows
    for row in csvreader:
        # Sort all the characters for each string alphabetically
        for i in range(0, len(row)):
            row[i] = ''.join(sorted(row[i]))

        # Add +1 to the counter if there are no matching strings
        if len(set(row)) == len(row):
            count += 1

# Print the answer
print count
