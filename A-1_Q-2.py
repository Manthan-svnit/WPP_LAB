# Write a program that generates 100 random integers that are either 0 or 1. Then find the
# longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
# zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.

import random
lis = []
for i  in range(100):
    lis.append(random.randint(0,1))
print(lis)

count = 0
max_count = 0
for i in lis:
    if i == 0:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print(max_count)