##############################################################################################################
#                               Developer: Charuta Shivanee Caullychurn
#                               LinkedIn: www.linkedin.com/in/charuta-shivanee-caullychurn-793390188
#                               Project: Grocery Inventory Management System
################################################################################################################



# firstly, i imported all the necessary libraries i'll be using to run my code
import csv
import random

# --- User Data (for demonstration purposes) ---

# Sample user credentials
customers = {"CUST123": "cust_password1", "CUST456": "cust_password2"}
grocery_manager = {"manager_name": "manager_password"}
cashier = {"cashier_id": "cashier_password"}

# 5 categories Define categories and sample items
categories = ["Dairy", "Bakery", "Produce", "Frozen Foods", "Beverages"]
products = [
    "Milk", "Bread", "Apples", "Ice Cream", "Juice",
    "Cheese", "Cake", "Bananas", "Frozen Pizza", "Soda",
    "Yogurt", "Muffins", "Tomatoes", "Frozen Veggies", "Water",
    "Butter", "Croissants", "Grapes", "Frozen Chicken", "Coffee",
]

# Define function to create inventory file
def create_inventory_file(filename="inventory.csv", num_products=500):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write headers
        writer.writerow(["Item Code", "Name", "Category", "Unit Price", "Quantity"])

        # Generate random products
        for i in range(num_products):
            item_code = f"ITM-{1000 + i}"
            name = random.choice(products)
            category = random.choice(categories)
            unit_price = round(random.uniform(1.0, 50.0), 2)  # Price between $1 and $50
            quantity = random.randint(1, 200)  # Quantity between 1 and 200
            writer.writerow([item_code, name, category, unit_price, quantity])

    print(f"{num_products} items have been written to {filename}")

# Call function to create the inventory file
create_inventory_file()

#---Login Function ---

def login():
    print("Welcome to the Grocery Inventory System")
    print("1. Customer\n2. Grocery Manager\n3. Cashier")
    user_type = input("Select your user type (1/2/3): ")

    if user_type == "1":
        customer_id = input("Enter Customer ID: ")
        password = input("Enter Password: ")
        if customers.get(customer_id) == password:
            print("Customer login successful!")
            return "customer"
        else:
            print("Invalid Customer ID or Password.")
            return None

    elif user_type == "2":
        manager_name = input("Enter Manager Name: ")
        password = input("Enter Password: ")
        if grocery_manager.get(manager_name) == password:
            print("Grocery Manager login successful!")
            return "grocery_manager"
        else:
            print("Invalid Manager Name or Password.")
            return None

    elif user_type == "3":
        cashier_id = input("Enter Cashier ID: ")
        password = input("Enter Password: ")
        if cashier.get(cashier_id) == password:
            print("Cashier login successful!")
            return "cashier"
        else:
            print("Invalid Cashier ID or Password.")
            return None

    else:
        print("Invalid selection. Please choose a valid user type.")
        return None

# --- Menu Functions ---

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Products")
        print("2. Search for a Product")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_products()
        elif choice == "2":
            search_product()
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def grocery_manager_menu():
    while True:
        print("\n--- Grocery Manager Menu ---")
        print("1. Add New Product")
        print("2. Update Product Details")
        print("3. Remove Product")
        print("4. View Inventory")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            remove_product()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def cashier_menu():
    while True:
        print("\n--- Cashier Menu ---")
        print("1. Process Sale")
        print("2. View Products")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            process_sale()
        elif choice == "2":
            view_products()
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# --- Placeholder functions for menu actions ---
def view_products():
    print("Displaying list of products...")

def search_product():
    print("Searching for a product...")

def add_product():
    print("Adding a new product...")

def update_product():
    print("Updating product details...")

def remove_product():
    print("Removing a product from inventory...")

def view_inventory():
    print("Viewing full inventory...")

def process_sale():
    print("Processing a sale...")

#---Main Program ---

def main():
    user_role = login()
    if user_role == "customer":
        customer_menu()
    elif user_role == "grocery_manager":
        grocery_manager_menu()
    elif user_role == "cashier":
        cashier_menu()
    else:
        print("Login failed. Exiting program.")

# Run the main function
if __name__ == "__main__":
    main()


