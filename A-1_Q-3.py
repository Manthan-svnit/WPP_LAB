# Write a program that asks the user to enter a length in feet. The program should then give
# the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
# meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
# enter a 2, then the program converts to yards, etc. While this can be done with if statements,
# it is much shorter with lists and it is also easier to add new conversions if you use lists

feet = float(input("Enter the length in feet: "))
print('''Type 1 to convert to inches
      Type 2 to convert to yards
      Type 3 to convert to miles
      Type 4 to convert to millimeters
      Type 5 to convert to centimeters
      Type 6 to convert to meters
      Type 7 to convert to kilometers''')

choice = int(input("Enter your choice: "))

# if choice == 1:
#     print(f"{feet} feet is equal to {feet * 12} inches")
# elif choice == 2:
#     print(f"{feet} feet is equal to {feet / 3} yards")
# elif choice == 3:
#     print(f"{feet} feet is equal to {feet / 5280} miles")
# elif choice == 4:
#     print(f"{feet} feet is equal to {feet * 304.8} millimeters")
# elif choice == 5:
#     print(f"{feet} feet is equal to {feet * 30.48} centimeters")
# elif choice == 6:
#     print(f"{feet} feet is equal to {feet * 0.3048} meters")
# elif choice == 7:
#     print(f"{feet} feet is equal to {feet * 0.0003048} kilometers")
# else:
#     print("Invalid choice")
conversions = [
        ("inches", 12),
        ("yards", 1/3),
        ("miles", 1/5280),
        ("millimeters", 304.8),
        ("centimeters", 30.48),
        ("meters", 0.3048),
        ("kilometers", 0.0003048)
    ]

if 1 <= choice <= 7:
    unit, factor = conversions[choice - 1]
    print(f"{feet} feet is equal to {feet * factor} {unit}")
else:
    print("Invalid choice")