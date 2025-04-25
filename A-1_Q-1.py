#(A) a list consisting of the integers 0 through 49.
my_list = list(range(50))
my_list = []
for i in range(50):
    my_list.append(i)
print(my_list)    

#(B) A list containing the squares of the integers 1 through 50.

squares = list(range(1,51))
squares = []

for i in range(1,51):
    squares.append(i**2)

print(squares)

#(C) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.

letters = []

for i in range(1,27):
    letters.append(i * chr(96 + i))

print(letters)