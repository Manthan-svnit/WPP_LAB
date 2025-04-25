# You are a student in a class of 10. Your class teacher assigns you a task of entering the
# names of all the students in the class. You finally want to display the names given the
# condition that the maximum allowed characters in a name is 15. As a fun task, reverse the
# names and display them. [Hint: Slicing works when you are selecting maximum characters]

# Initialize an empty list to store the names
names = []

for i in range(10):
    while True:
        name = input(f"Enter the name of student {i+1}: ")
        if len(name) <= 15:
            names.append(name)
            break
        else:
            print("Name should not exceed 15 characters. Please try again.")

reversed_names = [name[::-1] for name in names]
print("Reversed names of the students are:")
for name in reversed_names:
    print(name)
    