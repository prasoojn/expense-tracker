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