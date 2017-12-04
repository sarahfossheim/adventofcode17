import csv

# Count the lines with only unique words
count = 0

print sorted([1,2,3]) == sorted([1,2,3])
print sorted([1,2,3]) == sorted([3,1,2])

# Get the passphrase from the input file
with open('pt1.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in csvreader:



print count
