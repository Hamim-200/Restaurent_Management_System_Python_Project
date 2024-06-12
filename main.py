from FoodItem import FoodItem
from menu import Menu
from users import Customer, Admin, Employee
from restaurent import Restaurent
from orders import Order

# Initialize the restaurant
mamar_restaurent = Restaurent("Mamar Restaurant")

def customer_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    customer = Customer(name=name, email=email, phone=phone, address=address)
    
    while True:
        print(f"\nWelcome {customer.name}!")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")
        
        choice = input("Enter Your Choice: ").strip()
        if choice == '1':
            customer.view_menu(mamar_restaurent)
        elif choice == '2':
            item_name = input("Enter Item Name: ")
            item_quantity = int(input("Enter Item Quantity: "))
            customer.add_to_cart(mamar_restaurent, item_name, item_quantity)
        elif choice == '3':
            customer.view_cart()
        elif choice == '4':
            customer.pay_bill()
        elif choice == '5':
            break
        else:
            print("Invalid Input. Please enter a number between 1 and 5.")

def admin_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    admin = Admin(name=name, email=email, phone=phone, address=address)
    
    while True:
        print(f"\nWelcome {admin.name}!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employees")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")
        
        choice = input("Enter Your Choice: ").strip()
        if choice == '1':
            item_name = input("Enter Item Name: ")
            item_price = float(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item Quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_restaurent, item)
        elif choice == '2':
            name = input("Enter Employee Name: ")
            phone = input("Enter Employee Phone: ")
            email = input("Enter Employee Email: ")
            designation = input("Enter Employee Designation: ")
            age = int(input("Enter Employee Age: "))
            salary = float(input("Enter Employee Salary: "))
            address = input("Enter Employee Address: ")
            employee = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(mamar_restaurent, employee)
        elif choice == '3':
            admin.view_employee(mamar_restaurent)
        elif choice == '4':
            admin.view_menu(mamar_restaurent)
        elif choice == '5':
            item_name = input("Enter Item Name: ")
            admin.remove_item(mamar_restaurent, item_name)
        elif choice == '6':
            break
        else:
            print("Invalid Input. Please enter a number between 1 and 6.")

while True:
    print("\nWelcome to Mamar Restaurant Management System!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = input("Enter Your Choice: ").strip()
    if choice == '1':
        customer_menu()
    elif choice == '2':
        admin_menu()
    elif choice == '3':
        print("Thank you for using Mamar Restaurant Management System. Goodbye!")
        break
    else:
        print("Invalid Input. Please enter a number between 1 and 3.")
