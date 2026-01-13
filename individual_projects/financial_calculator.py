# NS 1st financial calculator 
def main():
    print("1. Savings Time Calculator")
    print("2. Compound Interest Calculator")
    print("3. Budget Allocator")
    print("4. Sale Price Calculator")
    print("5. Tip Calculator")

    choice = input("Choose an option: ")

    if choice == "1":
        savings()
    elif choice == "2":
        compound_interest()
    elif choice == "3":
        budget()
    elif choice == "4":
        sale_price()
    elif choice == "5":
        tip()


def savings():
    goal = float(input("Saving goal: "))
    contribution = float(input("Monthly contribution: "))
    months = goal / contribution
    print(f"It will take {int(months)} months to save ${goal:.2f}")


def compound_interest():
    amount = float(input("Starting amount: "))
    rate = float(input("Interest rate (%): ")) / 100
    years = int(input("Years: "))

    def calculate():  
        return amount * (1 + rate) ** years

    total = calculate()
    print(f"After {years} years you will have ${total:.2f}")


def budget():
    income = float(input("Monthly income: "))
    savings = income * 0.20
    food = income * 0.30
    entertainment = income * 0.10
    bills = income * 0.40

    print(f"Savings: ${savings:.2f}")
    print(f"Food: ${food:.2f}")
    print(f"Entertainment: ${entertainment:.2f}")
    print(f"Bills: ${bills:.2f}")


def sale_price():
    price = float(input("Original price: "))
    discount = float(input("Discount (%): "))
    new_price = price * (1 - discount / 100)
    print(f"Sale price: ${new_price:.2f}")


def tip():
    bill = float(input("Bill amount: "))
    percent = float(input("Tip percent: "))
    tip_amount = bill * percent / 100
    total = bill + tip_amount
    print(f"Tip: ${tip_amount:.2f}, Total: ${total:.2f}")


main()
