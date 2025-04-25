num = int(input("Enter number you want factorial: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"{num}! = {factorial}")