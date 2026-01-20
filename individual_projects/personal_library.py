# NS 1st Personal Library 

# Empty list to store books
library = []


# Show all books
def view():
    if library == []:
        print("\nNo books in library.\n")
    else:
        for book in library:
            print(book)
        print()


# Add a book
def add():
    title = input("Title: ")
    author = input("Author: ")
    library.append(title + " by " + author)
    print("\nBook added!\n")


# Remove a book
def remove():
    if library == []:
        print("\nLibrary is empty.\n")
        return

    for i in range(len(library)):
        print(i + 1, library[i])

    choice = int(input("Number to remove: "))
    library.pop(choice - 1)
    print("\nBook removed!\n")


# Search for a book
def search():
    word = input("Search word: ").lower()

    for book in library:
        if word in book.lower():
            print(book)
    print()


# Main menu
def main():
    print("Welcome to your Library!\n")

    while True:
        print("1. View")
        print("2. Add")
        print("3. Remove")
        print("4. Search")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            view()
        elif choice == "2":
            add()
        elif choice == "3":
            remove()
        elif choice == "4":
            search()
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice\n")


# Run program
main()