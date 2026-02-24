# NS 1st word counter

def read_document(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. A new file will be created.")
        return ""


def write_document(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)


def append_content(file_path, new_content):
    with open(file_path, "a") as file:
        file.write("\n" + new_content)


def count_words(text):
    words = text.split()
    return len(words)


def update_document_info(file_path, timestamp):
    content = read_document(file_path)

    word_count = count_words(content)

    update_text = f"\nWord Count: {word_count}\nLast Updated: {timestamp}\n"

    append_content(file_path, update_text)

    return word_count