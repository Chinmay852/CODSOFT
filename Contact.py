class ContactList:
    def __init__(self):
        self.contacts = {}
        self.contact_id_counter = 1
    
    def add_contact(self, name, phone_number, email, address):
        contact_info = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "address": address
        }
        self.contacts[self.contact_id_counter] = contact_info
        self.contact_id_counter += 1
        print("Contact added successfully.")
    
    def view_contact_list(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for contact_id, contact_info in self.contacts.items():
                print(f"ID: {contact_id}, Name: {contact_info['name']}, Phone: {contact_info['phone_number']}")
    
    def search_contact(self, query):
        results = []
        for contact_id, contact_info in self.contacts.items():
            if query.lower() in contact_info['name'].lower() or query in contact_info['phone_number']:
                results.append((contact_id, contact_info))
        if results:
            print("Search Results:")
            for result in results:
                print(f"ID: {result[0]}, Name: {result[1]['name']}, Phone: {result[1]['phone_number']}")
        else:
            print("No matching contacts found.")
    
    def update_contact(self, contact_id, new_name=None, new_phone_number=None, new_email=None, new_address=None):
        if contact_id not in self.contacts:
            print("Contact ID not found.")
            return
        contact_info = self.contacts[contact_id]
        if new_name:
            contact_info['name'] = new_name
        if new_phone_number:
            contact_info['phone_number'] = new_phone_number
        if new_email:
            contact_info['email'] = new_email
        if new_address:
            contact_info['address'] = new_address
        print("Contact updated successfully.")
    
    def delete_contact(self, contact_id):
        if contact_id not in self.contacts:
            print("Contact ID not found.")
            return
        del self.contacts[contact_id]
        print("Contact deleted successfully.")

def main():
    contact_list = ContactList()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_list.add_contact(name, phone_number, email, address)
        elif choice == "2":
            contact_list.view_contact_list()
        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            contact_list.search_contact(query)
        elif choice == "4":
            contact_id = int(input("Enter ID of the contact to update: "))
            new_name = input("Enter new name (leave blank to keep unchanged): ")
            new_phone_number = input("Enter new phone number (leave blank to keep unchanged): ")
            new_email = input("Enter new email (leave blank to keep unchanged): ")
            new_address = input("Enter new address (leave blank to keep unchanged): ")
            contact_list.update_contact(contact_id, new_name, new_phone_number, new_email, new_address)
        elif choice == "5":
            contact_id = int(input("Enter ID of the contact to delete: "))
            contact_list.delete_contact(contact_id)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
