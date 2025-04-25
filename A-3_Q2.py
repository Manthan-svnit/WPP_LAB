#Is Fibo

count = int(input("Enter the number of test cases: "))
for i in range(count):
    n = int(input("Enter a number: "))
    a = 0
    b = 1
    c = 0
    while c < n:
        c = a + b
        a = b
        b = c
    if c == n:
        print("IsFibo")
    else:
        print("IsNotFibo")