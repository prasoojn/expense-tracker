import sqlite3

DB_NAME = "expenses.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL CHECK (amount > 0),
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                note TEXT
            )
        """)

def add_expense(amount, category, date, note=""):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO expenses (amount, category, date, note) "
            "VALUES (?, ?, ?, ?)",
            (amount, category, date, note),
        )

def list_expenses():
    with get_connection() as conn:
        return conn.execute(
            "SELECT id, amount, category, date, note "
            "FROM expenses ORDER BY date"
        ).fetchall()

def update_expense(expense_id, amount, category, date, note=""):
    with get_connection() as conn:
        cur = conn.execute(
            "UPDATE expenses SET amount=?, category=?, date=?, note=? "
            "WHERE id=?",
            (amount, category, date, note, expense_id),
        )
        return cur.rowcount > 0

def delete_expense(expense_id):
    with get_connection() as conn:
        cur = conn.execute(
            "DELETE FROM expenses WHERE id=?", (expense_id,)
        )
        return cur.rowcount > 0

def monthly_total(month):  # month looks like "2026-10"
    with get_connection() as conn:
        row = conn.execute(
            "SELECT COALESCE(SUM(amount), 0) FROM expenses "
            "WHERE substr(date, 1, 7) = ?",
            (month,),
        ).fetchone()
        return row[0]

def totals_by_category(month):
    with get_connection() as conn:
        return conn.execute(
            "SELECT category, SUM(amount) FROM expenses "
            "WHERE substr(date, 1, 7) = ? "
            "GROUP BY category ORDER BY SUM(amount) DESC",
            (month,),
        ).fetchall()