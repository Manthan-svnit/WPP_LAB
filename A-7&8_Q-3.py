class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, name, initial_balance=0):
        if customer_id in self.customers:
            print(f"Customer with ID {customer_id} already exists.")
        else:
            self.customers[customer_id] = {'name': name, 'balance': initial_balance}
            print(f"Customer {name} added with ID {customer_id}.")

    def deposit(self, customer_id, amount):
        if customer_id in self.customers:
            self.customers[customer_id]['balance'] += amount
            print(f"Deposited {amount} to customer ID {customer_id}. New balance: {self.customers[customer_id]['balance']}")
        else:
            print(f"Customer with ID {customer_id} does not exist.")

    def withdraw(self, customer_id, amount):
        if customer_id in self.customers:
            if self.customers[customer_id]['balance'] >= amount:
                self.customers[customer_id]['balance'] -= amount
                print(f"Withdrew {amount} from customer ID {customer_id}. New balance: {self.customers[customer_id]['balance']}")
            else:
                print(f"Insufficient balance for customer ID {customer_id}.")
        else:
            print(f"Customer with ID {customer_id} does not exist.")

    def get_balance(self, customer_id):
        if customer_id in self.customers:
            return self.customers[customer_id]['balance']
        else:
            print(f"Customer with ID {customer_id} does not exist.")
            return None

bank = Bank()
bank.add_customer(1, "Alice", 1000)
bank.add_customer(2, "Bob", 500)

bank.deposit(1, 200)
bank.withdraw(2, 100)
print(f"Alice's balance: {bank.get_balance(1)}")
print(f"Bob's balance: {bank.get_balance(2)}")