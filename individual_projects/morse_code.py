# NS 1st Morse code translator 

# morse code translator

# english and morse code tuples
letters = ("a","b","c","d","e","f","g","h","i","j",
           "k","l","m","n","o","p","q","r","s","t",
           "u","v","w","x","y","z"," ")

morse = (".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
         "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
         "..-","...-",".--","-..-","-.--","--..","/")

# english to morse
def english_to_morse(text):
    text = text.lower()
    result = ""

    for char in text:
        if char in letters:
            result += morse[letters.index(char)] + " "
        else:
            result += "? "

    return result

# morse to english
def morse_to_english(code):
    result = ""
    symbols = code.split()

    for symbol in symbols:
        if symbol in morse:
            result += letters[morse.index(symbol)]
        else:
            result += "?"

    return result

# main menu
print("welcome to the morse code translator")

while True: 
    print("1. Morse Code to English")
    print("2. English to Morse Code")
    print("3. Exit")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        code = input("Enter morse code:\n")
        print("Your message says:")
        print(morse_to_english(code))

    elif choice == "2":
        text = input("Enter english text:\n")
        print("Your message says:")
        print(english_to_morse(text))

    elif choice == "3":
        print("goodbye")
        break

    else:
        print("invalid choice")