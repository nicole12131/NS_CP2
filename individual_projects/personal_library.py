# NS 1st Personal Library

import csv


library = []
file_name = "library.csv"
unsaved_changes = False
fields = ["title", "creator", "year", "genre"]


# Load from CSV file
def load():
    global library
    library = []
# create file libarry
    with open(file_name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
    print("New library file created.")


# Save to CSV file
def save():
    global unsaved_changes

    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(library)

    unsaved_changes = False
    print("Library saved!")


# Show simple list (title + creator)
def view_simple():
    if library == []:
        print("No items in library.")
    else:
        for i in range(len(library)):
            item = library[i]
            print(i + 1, "-", item["title"], "by", item["creator"])
    print()


# Show detailed list
def view_detailed():
    if library == []:
        print("No items in library.")
    else:
        for i in range(len(library)):
            item = library[i]
            print("\nItem", i + 1)
            print("Title:", item["title"])
            print("Creator:", item["creator"])
            print("Year:", item["year"])
            print("Genre:", item["genre"])
    print()


# Add item
def add():
    global unsaved_changes

    title = input("Title: ")
    creator = input("Creator: ")
    year = input("Year: ")
    genre = input("Genre: ")

    if title == "" or creator == "" or year == "" or genre == "":
        print("Invalid input. Try again.")
        return

    new_item = {
        "title": title,
        "creator": creator,
        "year": year,
        "genre": genre
    }

    library.append(new_item)
    unsaved_changes = True
    print("Item added!")


# Remove item
def remove():
    global unsaved_changes

    if library == []:
        print("Library is empty.")
        return

    view_simple()

    try:
        choice = int(input("Number to remove: ")) - 1
        if choice < 0 or choice >= len(library):
            print("Invalid number.")
            return
    except:
        print("Invalid input.")
        return

    library.pop(choice)
    unsaved_changes = True
    print("Item removed!")


# Update item
def update():
    global unsaved_changes

    if library == []:
        print("Library is empty.")
        return

    view_simple()

    try:
        choice = int(input("Number to update: ")) - 1
        if choice < 0 or choice >= len(library):
            print("Invalid number.")
            return
    except:
        print("Invalid input.")
        return

    item = library[choice]

    title = input("New Title (leave blank to keep): ")
    creator = input("New Creator (leave blank to keep): ")
    year = input("New Year (leave blank to keep): ")
    genre = input("New Genre (leave blank to keep): ")

    if title != "":
        item["title"] = title
    if creator != "":
        item["creator"] = creator
    if year != "":
        item["year"] = year
    if genre != "":
        item["genre"] = genre

    unsaved_changes = True
    print("Item updated!")


# Main menu
def main():
    load()
    print("Welcome to your Library!")

    while True:
        print("1. View Simple")
        print("2. View Detailed")
        print("3. Add")
        print("4. Remove")
        print("5. Update")
        print("6. Save")
        print("7. Exit")

        choice = input("Choice: ")

        if choice == "1":
            view_simple()
        elif choice == "2":
            view_detailed()
        elif choice == "3":
            add()
        elif choice == "4":
            remove()
        elif choice == "5":
            update()
        elif choice == "6":
            save()
        elif choice == "7":
            if unsaved_changes:
                answer = input("Save before exit? (y/n): ")
                if answer.lower() == "y":
                    save()
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


main()
