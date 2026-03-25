#NS 1st classes project
import random

# -------------------------
# Pet Class
# -------------------------
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.health = 100

    # feed pet
    def feed(self):
        self.hunger += 20
        self.happiness += 5
        print(f"{self.name} has been fed!")

    # play with pet
    def play(self):
        self.happiness += 20
        self.energy -= 10
        self.hunger += 10
        print(f"You played with {self.name}!")

    # sleep
    def sleep(self):
        self.energy += 30
        print(f"{self.name} is sleeping!")

    # random event
    def event(self):
        event = random.choice(["toy", "sick", "nothing"])
        if event == "toy":
            self.happiness += 10
            print(f"{self.name} found a toy! 😊")
        elif event == "sick":
            self.health -= 10
            print(f"{self.name} got sick... 🤒")

    # show status
    def status(self):
        print("\n--- STATUS ---")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Health: {self.health}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")

# -------------------------
# Main Program
# -------------------------
pets = []

print("🐾 Virtual Pet Simulator 🐾")

# create first pet
name = input("Enter pet name: ")
species = input("Enter species: ")
pets.append(Pet(name, species))

current = 0

while True:
    pet = pets[current]

    print("\nMAIN MENU")
    print(f"Current Pet: {pet.name}")
    print("1. Feed")
    print("2. Play")
    print("3. Sleep")
    print("4. Check Status")
    print("5. Create New Pet")
    print("6. Switch Pet")
    print("7. Quit")

    choice = input("Choose: ")

    if choice == "1":
        pet.feed()

    elif choice == "2":
        pet.play()

    elif choice == "3":
        pet.sleep()

    elif choice == "4":
        pet.status()

    elif choice == "5":
        name = input("Name: ")
        species = input("Species: ")
        pets.append(Pet(name, species))

    elif choice == "6":
        for i, p in enumerate(pets):
            print(i, p.name)
        current = int(input("Choose pet #: "))

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

    # random event after each action
    pet.event()
