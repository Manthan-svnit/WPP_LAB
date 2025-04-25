#The Love-Letter Mystery
def make_palindrome(s):
    changes = 0
    left = 0
    right = len(s) - 1
    
    while left < right:
        changes += abs(ord(s[left]) - ord(s[right]))        
        #abs = return the absolute value of argument
        #ord = return the unicode point for a one-character string
        left += 1
        right -= 1
        
    return changes
T = int(input("Enter number of test cases: \n"))

for _ in range(T):
    s = input("Enter the string: \n")
    print(make_palindrome(s))