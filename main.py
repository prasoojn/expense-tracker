import csv
from datetime import datetime

from db import (
    create_table, add_expense, list_expenses,
    update_expense, delete_expense,
    monthly_total, totals_by_category,
)

MENU = """
1. Add expense
2. List expenses
3. Edit expense
4. Delete expense
5. Monthly summary
6. Export to CSV
0. Exit
"""


def ask_amount():
    while True:
        try:
            amount = float(input("Amount: "))
            if amount > 0:
                return amount
            print("Amount must be positive.")
        except ValueError:
            print("Please enter a number.")


def ask_date():
    while True:
        text = input("Date (YYYY-MM-DD, blank = today): ").strip()
        if text == "":
            return datetime.today().strftime("%Y-%m-%d")
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Use the format YYYY-MM-DD.")


def ask_month():
    while True:
        text = input("Month (YYYY-MM): ").strip()
        try:
            datetime.strptime(text, "%Y-%m")
            return text
        except ValueError:
            print("Use the format YYYY-MM.")


def ask_id():
    while True:
        try:
            return int(input("Expense id: "))
        except ValueError:
            print("Please enter a whole number.")


def ask_details():
    amount = ask_amount()
    category = input("Category: ").strip().title() or "Other"
    date = ask_date()
    note = input("Note: ").strip()
    return amount, category, date, note


def show(rows):
    if not rows:
        print("No expenses found.")
        return
    for r in rows:
        print(f"{r[0]:>3} | {r[1]:>9.2f} | {r[2]:<12} | {r[3]} | {r[4]}")


def export_csv():
    rows = list_expenses()
    with open("expenses.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "amount", "category", "date", "note"])
        writer.writerows(rows)
    print(f"Exported {len(rows)} expenses to expenses.csv")


def main():
    create_table()
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        if choice == "1":
            amount, category, date, note = ask_details()
            add_expense(amount, category, date, note)
            print("Expense added.")
        elif choice == "2":
            show(list_expenses())
        elif choice == "3":
            expense_id = ask_id()
            amount, category, date, note = ask_details()
            if update_expense(expense_id, amount, category, date, note):
                print("Expense updated.")
            else:
                print("No expense with that id.")
        elif choice == "4":
            if delete_expense(ask_id()):
                print("Expense deleted.")
            else:
                print("No expense with that id.")
        elif choice == "5":
            month = ask_month()
            print(f"Total for {month}: {monthly_total(month):.2f}")
            for category, total in totals_by_category(month):
                print(f"  {category:<12} {total:>9.2f}")
        elif choice == "6":
            export_csv()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()