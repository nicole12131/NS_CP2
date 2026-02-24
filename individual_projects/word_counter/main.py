# NS 1st word counter 

from file_handling import read_document, write_document, append_content, update_document_info
from time_handling import get_current_timestamp


def display_menu():
    print("\n--- Document Word Count Updater ---")
    print("1. Update document info")
    print("2. View document")
    print("3. Add content to document")
    print("4. Exit")


def main():
    file_path = ""

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            file_path = input("\nEnter the exact file path for your document: ")

            timestamp = get_current_timestamp()
            word_count = update_document_info(file_path, timestamp)

            print(f"Document updated. Word count: {word_count}")

        elif choice == "2":
            if file_path == "":
                print("Please update document info first to select a file.")
            else:
                content = read_document(file_path)
                print("\nDocument content:")
                print(content)

        elif choice == "3":
            if file_path == "":
                print("Please update document info first to select a file.")
            else:
                print("\nEnter new content (press Enter twice to finish):")

                lines = []
                while True:
                    line = input()
                    if line == "":
                        break
                    lines.append(line)

                new_text = "\n".join(lines)

                append_content(file_path, new_text)
                print("Content added successfully.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()