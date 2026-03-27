#Develop a contact book that can save, edit, and search contacts
#handle error such as duplicate entries, emopty fields, and wrong phone number format



class DuplicateEntryError(Exception):
    pass

class EmptyFieldError(Exception):
    pass

class InvalidPhoneNumberError(Exception):
    pass


class ContactBook:
    def __init__(self):
        self.contacts = {}  

   
    def add_contact(self, name, phone):
        try:
            if name == "" or phone == "":
                raise EmptyFieldError("Name or phone number cannot be empty.")

            if name in self.contacts:
                raise DuplicateEntryError("Contact already exists.")

            if not phone.isdigit() or len(phone) != 10:
                raise InvalidPhoneNumberError("Phone number must be 10 digits.")

            self.contacts[name] = phone
            print("Contact saved successfully.")

        except Exception as e:
            print("Error:", e)


    def edit_contact(self, name, new_phone):
        try:
            if name not in self.contacts:
                raise KeyError("Contact not found.")

            if new_phone == "":
                raise EmptyFieldError("Phone number cannot be empty.")

            if not new_phone.isdigit() or len(new_phone) != 10:
                raise InvalidPhoneNumberError("Invalid phone number format.")

            self.contacts[name] = new_phone
            print("Contact updated successfully.")

        except Exception as e:
            print("Error:", e)

    
    def search_contact(self, name):
        try:
            if name == "":
                raise EmptyFieldError("Name cannot be empty.")

            if name not in self.contacts:
                raise KeyError("Contact not found.")

            print("Contact Found:", name, "-", self.contacts[name])

        except Exception as e:
            print("Error:", e)

    
    def display_contacts(self):
        print("\nContact List:")
        for name, phone in self.contacts.items():
            print(name, ":", phone)



book = ContactBook()

book.add_contact("Rahul", "9876543210")
book.add_contact("Amit", "9123456789")

book.search_contact("Rahul")

book.edit_contact("Rahul", "9998887776")

book.display_contacts()