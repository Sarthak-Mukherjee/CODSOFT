contacts = []

def add_cont(contacts, name, phone, email, address):
    cont = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
    contacts.append(cont)
    print(f"Contact {name} added successfully!")

def view_cont(contacts):
    for cont in contacts:
        print(f"Name: {cont['Name']}")
        print(f"Phone: {cont['Phone']}")
        print(f"Email: {cont['Email']}")
        print(f"Address: {cont['Address']}")
        print("\n")

def search_cont(contacts, name):
    for cont in contacts:
        if cont['Name'] == name:
            print(f"Name: {cont['Name']}")
            print(f"Phone: {cont['Phone']}")
            print(f"Email: {cont['Email']}")
            print(f"Address: {cont['Address']}")
            return
    print("Contact not found!")

def update_cont(contacts, name):
    for cont in contacts:
        if cont['Name'] == name:
            print("Enter new details of the contact:")
            n_name = input("New Name: ")
            n_phone = input("New Phone: ")
            n_email = input("New Email: ")
            n_address = input("New Address: ")

            cont['Name'] = n_name
            cont['Phone'] = n_phone
            cont['Email'] = n_email
            cont['Address'] = n_address

            print(f"Contact {name} updated!")
            return
    print(f"Contact {name} not found!")

def delete_cont(contacts, name):
    for cont in contacts:
        if cont['Name'] == name:
            contacts.remove(cont)
            print(f"Contact {name} deleted!")
            return
    print(f"Contact {name} not found!")

def main():
    while True:
        print("\n****CONTACT BOOK****")
        print("1. Add Contact\n2. View Contact\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit\nEnter your choice:")
        ch = input()

        if ch == '1':
            name = input("Enter Your Name: ")
            phone = input("Enter Your Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            add_cont(contacts, name, phone, email, address)
        elif ch == '2':
            view_cont(contacts)
        elif ch == '3':
            name = input("Enter name of the contact to be searched: ")
            search_cont(contacts, name)
        elif ch == '4':
            name = input("Enter contact name to update: ")
            update_cont(contacts, name)
        elif ch == '5':
            name = input("Enter contact name to delete: ")
            delete_cont(contacts, name)
        elif ch == '6':
            print("Exiting Contact Book!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()
