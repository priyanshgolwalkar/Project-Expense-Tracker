import os

# File to store the expenses
EXPENSES_FILE = "expenses.txt"

# Function to display the menu
def display_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expenses by Category")
    print("4. View Budget Status")
    print("5. Exit")

# Function to load expenses from the file
def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []
    with open(EXPENSES_FILE, 'r') as file:
        expenses = []
        for line in file.readlines():
            date, amount, category, description = line.strip().split(", ")
            expenses.append({"date": date, "amount": float(amount), "category": category, "description": description})
        return expenses

# Function to save expenses to the file
def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as file:
        for expense in expenses:
            file.write(f"{expense['date']}, {expense['amount']}, {expense['category']}, {expense['description']}\n")

# Function to add an expense
def add_expense(expenses):
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (e.g., groceries, entertainment, etc.): ")
    description = input("Enter a description: ")
    expenses.append({"date": date, "amount": amount, "category": category, "description": description})
    save_expenses(expenses)
    print(f"Expense of {amount} added!")

# Function to view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        for exp in expenses:
            print(f"{exp['date']}: {exp['category']} - {exp['description']} - ${exp['amount']}")

# Function to view expenses by category
def view_expenses_by_category(expenses):
    category = input("Enter the category: ")
    filtered_expenses = [exp for exp in expenses if exp['category'].lower() == category.lower()]
    if not filtered_expenses:
        print(f"No expenses found for category: {category}")
    else:
        for exp in filtered_expenses:
            print(f"{exp['date']}: {exp['category']} - {exp['description']} - ${exp['amount']}")

# Function to view the budget status
def view_budget_status(expenses):
    budget = float(input("Enter your monthly budget: "))
    total_expense = sum(exp['amount'] for exp in expenses)
    print(f"Total Expenses: ${total_expense}")
    print(f"Remaining Budget: ${budget - total_expense}")
    if total_expense > budget:
        print("Warning: You’ve exceeded your budget!")

# Main function to run the app
def main():
    expenses = load_expenses()

    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            view_expenses_by_category(expenses)
        elif choice == '4':
            view_budget_status(expenses)
        elif choice == '5':
            print("Exiting Expense Tracker application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
