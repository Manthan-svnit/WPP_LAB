n = int(input("Enter a number: "))
def sum_of_digits(n):  # Repeat until n is a single-digit number
    while n >= 10:
        sum = 0
        for i in str(n): # Convert n to a string to iterate over each digit
            sum += int(i) # Convert each digit back to an integer and add to sum
        n = sum # Set n to the sum of its digits    
    return n

print(sum_of_digits(n))