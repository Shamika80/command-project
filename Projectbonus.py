import re
import json

contacts = {}


def edit_contact():

 def delete_contact():
    identifier = input("Enter identifier of contact to delete: ")
    if identifier not in contacts:
        print("Contact not found.")
        return
    del contacts[identifier]
    print("Contact deleted successfully!")

def search_contact():

 def display_all_contacts():

  def export_contacts():
    filename = input("Enter filename (e.g., contacts.txt): ")
    with open(filename, 'w') as file:
        for identifier, contact in contacts.items():
            file.write(f"{identifier}: {contact}\n")
    print("Contacts exported successfully!")

def import_contacts():
    filename = input("Enter filename: ")
    try:
        with open(filename, 'r') as file:
            for line in file:
                identifier, contact_str = line.strip().split(': ')
                contacts[identifier] = eval(contact_str)  
        print("Contacts imported successfully!")
    except (FileNotFoundError, ValueError):
        print("Error importing contacts.")

def add_category(identifier, category):
    
 def remove_category(identifier, category):
    
  def backup_contacts():
    
    def restore_contacts():
    

     while True:
        "display_menu"()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            "add_contact"()
        elif choice == 2:
            edit_contact()
        elif choice == 3:
            "delete_contact"()
        elif choice == 4:
            search_contact()
        elif choice == 5:
            "display_all_contacts"()
        elif choice == 6:
            "export_contacts"()
        elif choice == 7:
            import_contacts()
        
        elif choice == 8:
            "break"
        else:
            print("Invalid input. Please enter a number.")
    except ValueError:
        print("Invalid input. Please enter a number.")    