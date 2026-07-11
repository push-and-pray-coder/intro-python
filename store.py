from catalog import catalog # import file catalog getting catalog dictionary
# global variable
cart = [] # empty list
# HELPER FUNCTIONS
def header(text):
    print("------------------")
    print(text)
    print("------------------")
def menu():
    print("Menu")
    print("1. View Catalog")
    print("2. Search Product")
    print("3. View Cart")
    # ADD MORE FEATURES
    print("Q. Quit")
# CATALOG CART AND FUNCTION
def print_catalog():
    header("- Our Catalog -")
    for prod in catalog:  # Ljust means left justify. 15 spaces to the right
        print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')
    
    answer = input("Type ID to add (N to close): ")
    if answer.lower() == "n":
        return
    else:
        add_product_to_cart(answer)
def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod) # adds product to the cart
            print(f'{prod["title"]} added to your cart.')
            break  # stop after finding the product
    if not found:
        print("**ERROR: Invalid ID")
        
def search_product():
    text = input("Search Product: ").lower()
    found = False
    for prod in catalog:
        if text in prod["title"].lower():
            found = True
            print(f'Found: ID {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')
            choice = input("Do you want to add this item to your cart? (y/n)")
            if choice.lower() == "y":
                add_product_to_cart(prod["id"])
            break # stop after first match
    if not found:
        print("Sorry, this item dosent exist")
def view_cart():
    header("Your Cart")
    if not cart:
        print("Your cart is empty.")
    else:
        for prod in cart:
            print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f} |')
        
# MAIN PROGRAM LOOP
option = ""
while option != "q" and option != "Q":
    header("Welcome to Store xy")
    menu()
    option = input("Choose an option: ")
    if option == "1":
        print_catalog()
    elif option == "2":
        search_product()
    elif option == "3":
        view_cart()
    elif option == "q" or option == "Q":
        print("good bye")
        break
    else:
        print("** ERROR: invalid option")