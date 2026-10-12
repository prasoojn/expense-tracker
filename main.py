from db import *

create_table()
add_expense(150, "Food", "2026-10-12", "Lunch")
add_expense(60, "Travel", "2026-10-13", "Bus")
add_expense(200, "Food", "2026-10-14", "Dinner")

print(monthly_total("2026-10"))
print(totals_by_category("2026-10"))
print(update_expense(1, 180, "Food", "2026-10-12", "Lunch + juice"))
print(delete_expense(2))
print(list_expenses())