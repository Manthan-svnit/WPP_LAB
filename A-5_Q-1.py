# Maximizing XOR
L = int(input("Enter value of L: \n"))
R = int(input("Enter value of R: \n"))

max_xor = 0

for i in range(L, R + 1):
    for j in range(i, R + 1):
        xor_value = i ^ j
        if xor_value > max_xor:
            max_xor = xor_value

print(f"The maximum XOR value between {L} and {R} is: {max_xor}")