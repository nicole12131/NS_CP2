# NS 1st Random password generator 

# define main function 

# Ask the user to type the number for the action that they like to perform
# 1. Generate Passwords
# 2. Exit

def main(): 
    print("1. Generate password ")
    print("2. Exit ")
    action = input("Type the number for the action you would like to perform: ")

# if user choose 1
# Ask user how long the password need to be
# Ask if the password needs lowercase letters
# Ask if the password needs uppercase letters
# Ask if the password needs numbers
# Ask if password needs special characters 

    if action == "1":
        length = input("How long does the password needs to be: ")
        lower = input("Does the password need lowercase letters (Y/N): ")
        upper = input("Does the password need uppercase letters (Y/N): ")
        num = input("Does the password need numbers letters (Y/N): ")

# if user choose 2 
# print thanks for using the program 

    if action == "2":
        print(" thank you for using this pogram bye bye ")
# define function for how long the password needs to be

    def password_length():

# define function for lowercase letters in password 

    def password_lowecase():




# define function for uppercase letters in password 

# define a function for numbers in password 

# define function for special characters in password 

# print possible passwords

main()


    
   
    









