# --- Part Two ---
#
# Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.
#
# Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.
#
# How many steps does it now take to reach the exit?
#


import csv

arr = []

with open('pt1.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in csvreader:
        arr.append(int(row[0]))

arr_length = len(arr)
i = 0
count = 0

while i < arr_length:
    j = i
    j += arr[i]
    if arr[i] >= 3:
        arr[i] -= 1
    else:
        arr[i] += 1
    i = j
    count += 1

print count
