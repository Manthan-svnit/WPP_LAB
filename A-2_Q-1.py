# Write a program that asks the user to enter a word and then capitalizes every other letter of
# that word. So, if the user enters rhinoceros, the program should print rHiNoCeRoS.

word = input("Enter a word: ")
for i in word:
    if word.index (i) % 2 != 0:
        print(i.upper(),end="")
    else:
        print(i,end = "")
