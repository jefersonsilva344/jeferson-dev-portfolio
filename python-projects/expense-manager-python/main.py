



```python
import csv
from datetime import datetime


FILE = "expenses.csv"


def add_expense():
    description = input("Expense description: ")
    amount = float(input("Amount: "))

    date = datetime.now().strftime("%d/%m/%Y")

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            [description, amount, date]
        )

    print("Expense added successfully!")


def show_expenses():

    try:
        with open(FILE, "r") as file:

            reader = csv.reader(file)

            total = 0

            for row in reader:
                print(row)

                total += float(row[1])


            print("----------------")
            print(f"Total: R$ {total:.2f}")

    except FileNotFoundError:
        print("No expenses found.")


while True:

    print("""
    💰 Expense Manager

    1 - Add expense
    2 - Show expenses
    3 - Exit
    """)

    option = input("Choose: ")


    if option == "1":
        add_expense()

    elif option == "2":
        show_expenses()

    elif option == "3":
        break

    else:
        print("Invalid option")
