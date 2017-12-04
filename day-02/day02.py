import csv

# Set the count to 0
count = 0

# Open the csv file
with open('day02.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='	', quotechar='|')

    # Loop through all the rows
    for row in csvreader:

        # Convert every item to an int, then add the max - min to the count
        row = map(int, row)
        count += (max(row) - min(row))

print count
