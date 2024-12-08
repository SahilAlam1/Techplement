import re
from tabulate import tabulate

contacts = {}

def is_valid_email(email):
    """Validates email using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

while True:
    print("\nWelcome to Contact Management System\n")
    print("1. Create Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Exit\n")

    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 7:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            name = input("Enter your name: ")
            if name in contacts:
                print(f"Contact name '{name}' already exists!")
            else:
                while True:
                    age = input("Enter age: ")
                    if not age.isdigit():
                        print("Age should be a number.")
                    else:
                        age = int(age)
                        if age <= 0:
                            print("Age should be a positive number.")
                        else:
                            break

                while True:
                    email = input("Enter email: ")
                    if not is_valid_email(email):
                        print("Please enter a valid email address.")
                    else:
                        break

                while True:
                    number = input("Enter Mobile number: ")
                    if not number.isdigit() or len(number) != 10:
                        print("Please enter a valid 10-digit mobile number.")
                    else:
                        break

                contacts[name] = {"age": age, "email": email, "number": number}
                print(f"Contact '{name}' has been created successfully.")

        elif choice == 2:
            if not contacts:
                print("No contacts available.")
            else:

                table = []
                for name, details in contacts.items():
                    table.append([name, details["age"], details["email"], details["number"]])

                print("\nContacts:")
                print(tabulate(table, headers=["Name", "Age", "Email", "Phone Number"], tablefmt="grid"))

        elif choice == 3:
            name = input("Enter the name of the contact to update: ")
            if name in contacts:
                while True:
                    age = input("Enter updated age: ")
                    if not age.isdigit():
                        print("Age should be a number.")
                    else:
                        age = int(age)
                        if age <= 0:
                            print("Age should be a positive number.")
                        else:
                            break

                while True:
                    email = input("Enter updated email: ")
                    if not is_valid_email(email):
                        print("Please enter a valid email address.")
                    else:
                        break

                while True:
                    number = input("Enter updated Mobile number: ")
                    if not number.isdigit() or len(number) != 10:
                        print("Please enter a valid 10-digit mobile number.")
                    else:
                        break

                contacts[name] = {"age": age, "email": email, "number": number}
                print(f"Contact '{name}' has been updated.")
            else:
                print(f"Contact name '{name}' does not exist.")

        elif choice == 4:
            name = input("Enter the name of the contact to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact '{name}' has been deleted successfully!")
            else:
                print(f"Contact name '{name}' does not exist.")

        elif choice == 5:
            search_name = input("Enter contact name to search: ")
            found = False
            for name, contact in contacts.items():
                if search_name.lower() in name.lower():
                    print(f"\nName: {name}\nAge: {contact['age']}\nEmail: {contact['email']}\nNumber: {contact['number']}")
                    found = True
            if not found:
                print(f"Contact name '{search_name}' does not exist.")

        elif choice == 6:
            print(f"Total contacts: {len(contacts)}")

        elif choice == 7:
            print("Goodbye!... Closing the program")
            break

    except ValueError:
        print("Invalid input! Please enter a number.")

