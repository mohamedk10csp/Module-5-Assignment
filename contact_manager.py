
# Module 5 Assignment

contacts = {}


class DuplicateContactError(Exception):
    """Error raised when a contact already exists."""
    pass


def add_contact(name, phone):
    """Add a new contact."""
    if name in contacts:
        raise DuplicateContactError("Contact already exists.")

    contacts[name] = phone
    print(f"Added {name} to contacts.")


def find_contact(name):
    """Find a contact's phone number."""
    try:
        phone = contacts[name]
        print(f"{name}: {phone}")
        return phone
    except KeyError:
        print("Contact not found.")
        return None


def delete_contact(name):
    """Delete a contact."""
    try:
        del contacts[name]
        print(f"Deleted {name}.")
    except KeyError:
        print("Contact not found.")


def main():
    """Display the contact manager menu."""
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")

            try:
                add_contact(name, phone)
            except DuplicateContactError as e:
                print(e)

        elif choice == 2:
            name = input("Enter name to find: ")
            find_contact(name)

        elif choice == 3:
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
