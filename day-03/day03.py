# Taxicab distance formula:
# d = |x2 - x1| + |y2 - y1|

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23  24  25

# Data from square 1 is carried 0 steps, since it's at the access port.
# Data from square 12 is carried 3 steps, such as: down, left, left.
# Data from square 23 is carried only 2 steps: up twice.
# Data from square 1024 must be carried 31 steps.

# 65  64  63  62  61  60  59  58  57
# 66  37  36  35  34  33  32  31  56
# 67  38  17  16  15  14  13  30  55  88
# 68  39  18   5   4   3  12  29  54  87
# 69  40  19   6   1   2  11  28  53  86
# 70  41  20   7   8   9  10  27  52  85
# 71  42  21  22  23  24  25  26  51  84
# 72  43  44  45  46  47  48  49  50  83
# 73  74  75  76  77  78  79  80  81  82

import math
import sys

# Get the columns and rows
number = int(sys.argv[1])

# Get nearest odd square root
root = round(math.sqrt(number))
if root % 2 == 0:
    print number - (root * root) + (root - 1)
else:
    print number - (root * root)
