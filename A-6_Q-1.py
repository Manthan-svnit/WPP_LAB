class Password_manager: 
    def __init__(self):
        self.old_pass = []
        
        
    def get_password(self):
        return self.old_pass[-1] if self.old_pass else None
        # this gets the last item from the old_pass list,which represent current password
    
    def set_password(self,new_password):
        if new_password not in self.old_pass:
            self.old_pass.append(new_password)
            print("Password updated successfully. ")
        else:
            print("Error: This password already exists choose a different one. ")
            
    def is_correct(self,password):
        return password == self.get_password()
    
pwd_manager = Password_manager()

while True:
    print("1. Set a new password: ")
    print("2. Get current password: ")
    print("3. Check password: ")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        new_password = input("Enter new password: ")
        pwd_manager.set_password(new_password)
        
    elif choice == "2":
        print("current Password: ",pwd_manager.get_password())
    elif choice == "3":
        check_password = input("Enter password to check: ")
        if pwd_manager.is_correct(check_password):
            print("Password is correct. ")
        else: 
            print("Password is incorrect ")
    elif choice == "4":
        print("Exiting.....")
        break
    else:
        print('''Invalid choice.
              please try again ''')