#swap two variable without using third variable

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"after swaping num1 = {num1} num2 = {num2}")