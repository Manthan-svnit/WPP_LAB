# Write a program that repeatedly asks the user to enter product names and prices. Store all
# of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a
# product name and print the corresponding price or a message if the product is not in the
# dictionary.

products = {}

while True:
    product_name = input("Enter product name (or 'done' to finish): ")
    if product_name.lower() == 'done':
        break
    price = input("Enter price: ")
    if price.replace('.', '', 1).isdigit():
        products[product_name] = float(price)
    else:
        print("Invalid price. Please enter a number.")

while True:
    query = input("Enter product name to get the price (or 'done' to finish): ")
    if query.lower() == 'done':
        break
    if query in products:
        print(f"The price of {query} is {products[query]}")
    else:
        print("Product not found.")