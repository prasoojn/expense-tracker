from db import create_table, add_expense, list_expenses

create_table()
add_expense(150, "Food", "2026-10-12", "Lunch")
print(list_expenses())