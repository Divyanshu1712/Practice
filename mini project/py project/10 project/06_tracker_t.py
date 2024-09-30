from datetime import datetime

# Global dictionary to store expenses by category
expenses = {}

def add_expense(category):
    """
    Adds an expense to a specified category.
    Each expense includes a name, amount, and date.
    """
    print(f"\nYou are now adding expenses to the {category.upper()} category.")
    print("Type 'EXIT' when you're done.")

    while True:
        expense_name = input("Enter expense name (or 'EXIT' to stop): ").strip().upper()

        if expense_name == 'EXIT':
            break

        # Ensure valid input for amount
        try:
            amount = float(input(f"Enter the amount for {expense_name}: ").strip())
        except ValueError:
            print("Invalid amount! Please enter a valid number.")
            continue

        # Get current date
        current_date = datetime.now().strftime("%d-%m-%Y")

        # Add the expense to the category
        if category not in expenses:
            expenses[category] = []

        expenses[category].append({
            'Expense': expense_name,
            'Amount': amount,
            'Date': current_date
        })

        print(f"Added {expense_name} with amount {amount} on {current_date}.")

    print(f"\nFinished adding expenses to {category.upper()}.")
    return main_menu()

def view_expenses():
    """
    Displays all expenses organized by category.
    Also calculates and displays the total amount spent.
    """
    if not expenses:
        print("\nNo expenses recorded yet!")
        return main_menu()

    print("\nExpenses by category:")
    total_amount = 0

    for category, items in expenses.items():
        print(f"\nCategory: {category.upper()}")
        category_total = sum(item['Amount'] for item in items)
        total_amount += category_total

        for item in items:
            print(f"  - {item['Expense']}: {item['Amount']} (Date: {item['Date']})")
        print(f"  >> Total for {category.upper()}: {category_total}")

    print(f"\nOverall Total Expenses: {total_amount}")
    return main_menu()

def main_menu():
    """
    Displays the main menu and prompts the user to choose an action.
    """
    print("\nEXPENSE TRACKER - Main Menu")
    print("1. Add Home Expenses")
    print("2. Add Rent Expenses")
    print("3. Add Bills Expenses")
    print("4. Add Miscellaneous Expenses")
    print("5. View All Expenses")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    match choice:
        case '1':
            add_expense('Home')
        case '2':
            add_expense('Rent')
        case '3':
            add_expense('Bills')
        case '4':
            add_expense('Miscellaneous')
        case '5':
            view_expenses()
        case '6':
            print("Exiting the Expense Tracker. Have a nice day!")
            exit()
        case _:
            print("Invalid choice! Please enter a valid option.")
            return main_menu()

if __name__ == '__main__':
    main_menu()
