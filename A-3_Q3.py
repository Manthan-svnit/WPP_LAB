#Utopian Tree

def utopianTree(n):
    height = 1
    for i in range(n):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1
    return height

count = int(input("Enter the number of test cases: "))
for i in range(count):
    n = int(input("Enter nmber of cycles: "))
    print(utopianTree(n))