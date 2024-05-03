import re

contacts = {}  # Main dictionary to store contacts

def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def add_contact():
    while True:
        identifier = input("Enter unique identifier (phone number or email): ")
        if identifier in contacts:
            print("Identifier already exists. Please use a different one.")
        else:
            break

    name = input("Enter name: ")
    phone = get_valid_input("Enter phone number: ", r"^\d{10}$")  # Regex for 10-digit number
    email = get_valid_input("Enter email: ", r"^[^@]+@[^@]+\.[^@]+$")  # Basic email regex

    contacts[identifier] = {
        "name": name,
        "phone": phone,
        "email": email,
        "additional_info": {}  # For additional information
    }
    print("Contact added successfully!")

def edit_contact():
    identifier = input("Enter identifier of contact to edit: ")
    if identifier not in contacts:
        print("Contact not found.")
        return

    print("What would you like to edit?")
    print("1. Name")
    print("2. Phone number")
    print("3. Email")
    print("4. Additional information")

    # Input and validation similar to add_contact() ...

def delete_contact():
    # (Implementation similar to edit_contact)
    pass

def search_contact():
    # (Implementation similar to edit_contact)
    pass

def display_all_contacts():
    # ...
    pass

def export_contacts():
    # ...
    pass

def import_contacts():
    # ...
    pass

def get_valid_input(prompt, pattern):
    """Gets validated input using a regular expression."""
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

# Main program loop
while True:
    display_menu()
    try:
        choice = int(input("Enter your choice: "))
        # ... (Handle choices using if/elif statements)
    except ValueError:
        print("Invalid input. Please enter a number.")