def reverse_number(n):
    rev = 0
    while n > 0:
        remainder = n % 10
        rev = (rev * 10) + remainder
        n = n // 10
    return rev

number = int(input("Enter a number: "))
print("Reversed number:", reverse_number(number))