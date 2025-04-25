# num = (input("Enter a number: "))

# d = [int(d) for d in str(num)]

# count = 1
# for i in range(1,len(num)):
#     if(num % d == 0):
#         count += 1
    
# print(count)
def count_dividing_digits(num):
    num_str = str(num)
    count = 0

    for digit_char in num_str:
        digit = int(digit_char) 
        if digit != 0 and num % digit == 0: 
            count += 1
    
    return count


T = int(input("Enter number of test cases: "))

results = []
for _ in range(T):
    N = int(input("Enter the number: "))
    results.append(count_dividing_digits(N))

for result in results:
    print(result)
