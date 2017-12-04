import csv

# Set the count to 0
count = 0

# Open the csv file
with open('day02-pt2.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='	', quotechar='|')

    # Loop through all the rows
    for row in csvreader:

        # Convert every item to an int, then add the max - min to the count
        row = map(int, row)
        for i in range(0, len(row)):
            for j in range(0, len(row)):
                if i != j and row[j] != 0 and row[i] % row[j] == 0:
                    count += (row[i] / row[j])
                    break

print count
