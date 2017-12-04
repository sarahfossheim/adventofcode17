import sys

# Get the string and string length that's passed in from the terminal
arg = sys.argv[1]
length = len(arg)

# Count characters
count = 0

# Loop through the string and count identical characters
for i in range(0, length):
    j = i + 1
    if j == length:
        j = 0
    if arg[i] == arg[j]:
        count += int(arg[i])

print(count)
