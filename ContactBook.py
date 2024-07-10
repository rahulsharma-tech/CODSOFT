class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact.name} - {contact.phone_number}")

    def search_contact(self, search_term):
        results = []
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone_number):
                results.append(contact)
        
        if not results:
            print("No matching contacts found.")
        else:
            print(f"Search results for '{search_term}':")
            for contact in results:
                print(f"{contact.name} - {contact.phone_number}")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Updating contact '{contact.name}':")
                new_phone = input(f"Enter new phone number (current: {contact.phone_number}): ")
                new_email = input(f"Enter new email (current: {contact.email}): ")
                new_address = input(f"Enter new address (current: {contact.address}): ")

                # Update contact details
                contact.phone_number = new_phone if new_phone else contact.phone_number
                contact.email = new_email if new_email else contact.email
                contact.address = new_address if new_address else contact.address

                print(f"Contact '{contact.name}' updated successfully.")
                return
        
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{contact.name}' deleted successfully.")
                return
        
        print(f"Contact '{name}' not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("\nAdding New Contact:")
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            print("\nViewing Contact List:")
            contact_book.view_contacts()

        elif choice == '3':
            print("\nSearching Contact:")
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)

        elif choice == '4':
            print("\nUpdating Contact:")
            name = input("Enter name of contact to update: ")
            contact_book.update_contact(name)

        elif choice == '5':
            print("\nDeleting Contact:")
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("\nExiting Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
