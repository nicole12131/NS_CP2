# NS 1st Random password generator 

import random
import string


#   Receive password length and allowed characters
#   Create an empty password
#   Repeat for the length of the password
#       Randomly choose a character from allowed list
#       Add character to password
#   Return completed password

def generate_password(length, characters):
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password


#   Ask user for password length
#   Ask user which character types to include
#   Build a list of allowed characters
#   If no characters were selected
#       Display error message
#       Return to menu
#   Generate and display 4 passwords

def generate_passwords():
    length = int(input("How long does the password need to be: "))

    use_lower = input("Include lowercase letters (Y/N): ").upper() == "Y"
    use_upper = input("Include uppercase letters (Y/N): ").upper() == "Y"
    use_numbers = input("Include numbers (Y/N): ").upper() == "Y"
    use_special = input("Include special characters (Y/N): ").upper() == "Y"

    characters = ""

    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*"

    if characters == "":
        print("You must choose at least one option.")
        return

    print("Possible Passwords:")

    for _ in range(4):
        print(generate_password(length, characters))

#   Display program title
#   Loop until user chooses to exit
#       Display menu options
#       Get user choice
#       If choice is 1
#           Generate passwords
#       Else if choice is 2
#           Exit program
#       Else
#           Display error message

def main():
    print("Password Generator")

    while True:
        print("\nMAIN MENU")
        print("1. Generate Passwords")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            generate_passwords()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


#   Call the main function to start the program

main()
