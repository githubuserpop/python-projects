import sys
from collections import OrderedDict
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = OrderedDict()

    def add_expense(self, category, amount):
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append({"amount": amount, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "action": "Added"})
        self.view_expenses()
        self.save_expenses()

    def edit_expense(self, category, expense_number, new_amount):
        self.expenses[category][expense_number - 1]["amount"] = new_amount
        self.expenses[category][expense_number - 1]["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.expenses[category][expense_number - 1]["action"] = "Edited"
        self.view_expenses()
        self.save_expenses()

    def delete_expense(self, category, expense_number):
        self.expenses[category][expense_number - 1]["action"] = "Deleted"
        self.expenses[category][expense_number - 1]["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_expenses()
        del self.expenses[category][expense_number - 1]
        if not self.expenses[category]:
            del self.expenses[category]
        self.view_expenses()

    def view_expenses(self):
        print("\n" + "-" * 50)
        total = 0
        for category, expenses in self.expenses.items():
            print(f"Category: {category}")
            for i, expense in enumerate(expenses, start=1):
                print(f"  {i}. Amount: {expense['amount']}, Date: {expense['date']}")
                total += expense['amount']
        print(f"Total Expenses: {total}")
        print("-" * 50 + "\n")

    def view_expenses_by_category(self, category):
        print("\n" + "-" * 50)
        total = 0
        for i, expense in enumerate(self.expenses[category], start=1):
            print(f"  {i}. Amount: {expense['amount']}, Date: {expense['date']}")
            total += expense['amount']
        print(f"Total Expenses for {category}: {total}")
        print("-" * 50 + "\n")

    def save_expenses(self):
        for category, expenses in self.expenses.items():
            with open(f'{category}_expenses.txt', 'w') as f:
                f.write(f"Category: {category}\n")
                for expense in expenses:
                    f.write(f"  Amount: {expense['amount']}, Date: {expense['date']}, Action: {expense['action']}\n")
def main():
    expense_tracker = ExpenseTracker()
    while True:
        print("\n" + "=" * 50)
        print(" " * 15 + "EXPENSE TRACKER")
        print("=" * 50 + "\n")
        print("1. Add expense")
        print("2. Edit expense")
        print("3. Delete expense")
        print("4. View expenses")
        print("5. View expenses by category")
        print("6. Exit")
        print("\n" + "=" * 50 + "\n")
        print("Note: Please enter expenses in the following format: ")
        print("Category: 'category_name', Amount: 'amount'")
        print("Example: Category: 'Groceries', Amount: '50.5'")
        print("\n" + "=" * 50 + "\n")
        choice = input("Enter your choice: ")
        if choice in ['2', '3', '5']:
            print("\n" + "-" * 50)
            print(" " * 15 + "SELECT CATEGORY")
            print("-" * 50 + "\n")
            categories = list(expense_tracker.expenses.keys())
            for i, category in enumerate(categories, start=1):
                print(f"{i}. {category}")
            category_index = int(input("Select a category by its number: ")) - 1
            category = categories[category_index]
        if choice == '1':
            print("\n" + "-" * 50)
            print(" " * 15 + "ADD EXPENSE")
            print("-" * 50 + "\n")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            expense_tracker.add_expense(category, amount)
            print("\n" + "*" * 50)
            print("Expense added successfully!")
            print("*" * 50 + "\n")
        elif choice == '2':
            print("\n" + "-" * 50)
            print(" " * 15 + "EDIT EXPENSE")
            print("-" * 50 + "\n")
            expense_number = int(input("Enter expense number to edit: "))
            new_amount = float(input("Enter new amount: "))
            expense_tracker.edit_expense(category, expense_number, new_amount)
            print("\n" + "*" * 50)
            print("Expense edited successfully!")
            print("*" * 50 + "\n")
        elif choice == '3':
            print("\n" + "-" * 50)
            print(" " * 15 + "DELETE EXPENSE")
            print("-" * 50 + "\n")
            expense_number = int(input("Enter expense number to delete: "))
            expense_tracker.delete_expense(category, expense_number)
            print("\n" + "*" * 50)
            print("Expense deleted successfully!")
            print("*" * 50 + "\n")
        elif choice == '4':
            print("\n" + "-" * 50)
            print(" " * 15 + "VIEW EXPENSES")
            print("-" * 50 + "\n")
            expense_tracker.view_expenses()
        elif choice == '5':
            print("\n" + "-" * 50)
            print(" " * 15 + "VIEW EXPENSES BY CATEGORY")
            print("-" * 50 + "\n")
            expense_tracker.view_expenses_by_category(category)
        elif choice == '6':
            print("\n" + "-" * 50)
            print(" " * 15 + "EXITING PROGRAM")
            print("-" * 50 + "\n")
            sys.exit()
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()