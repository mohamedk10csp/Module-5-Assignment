# Robust Contact Manager

This project is a python contact manager to manage contact addition, search and deletion. The purpose was to enhance the initial program with correction

# Issues fixed
1. Made the program safer by adding in an exception for KeyErrors in case a contact is not found or is deleted
2. Improved user input to include Try/Except VauleError
3. Developed custom DuplicateContactError to avoid duplicate contacts
4. Included additional messages to clarify the error information

# Testing
Wrote 6 unit tests with the unittest framework in Python. The test evaluate adding, finding and deletion of contact, including missing and duplicate contacts 

All 6 tests were succesful 

# How to run the program
Open the terminal and enter:
python3 contact_manager.py

# How to run the tests
Enter: python3 -m unittest test_contact_manager.py

# Video Link 
