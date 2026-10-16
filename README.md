##### \# Expense Tracker

##### 

##### A command-line app to record and summarise personal expenses, built with Python and SQLite.

##### 

##### \## Features

##### \- Add, list, edit and delete expenses

##### \- Monthly total and per-category summary

##### \- Export all expenses to CSV

##### \- Input validation (positive amounts, valid dates)

##### \- Automated tests with pytest

##### 

##### \## Tech stack

##### Python 3.11, SQLite (built-in `sqlite3` module), pytest

##### 

##### \## How to run

##### ```

##### git clone https://github.com/prasoojn/expense-tracker.git

##### cd expense-tracker

##### python main.py

##### ```

##### 

##### \## How to run the tests

##### ```

##### pip install pytest

##### python -m pytest -v

##### ```

##### 

##### \## Project structure

##### \- `SPEC.md`: what the app must do (written before the code)

##### \- `db.py`: database layer (all SQL lives here)

##### \- `main.py`: command-line menu and input validation

##### \- `tests/test\_db.py`: automated tests for the database layer

##### 

##### \## Design notes

##### \- SQL uses `?` placeholders (parameterised queries) to prevent SQL injection

##### \- A `CHECK (amount > 0)` rule enforces positive amounts in the database itself

##### \- Dates are stored as `YYYY-MM-DD` text so they can be filtered by month

##### \- Tests use a temporary database, so real data is never touched

##### 

##### \## Possible future improvements

##### Budget limits, charts, a web interface.

