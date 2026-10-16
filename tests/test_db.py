import sqlite3

import pytest

import db


@pytest.fixture(autouse=True)
def temp_db(tmp_path, monkeypatch):
    # Every test gets its own empty database file
    monkeypatch.setattr(db, "DB_NAME", str(tmp_path / "test.db"))
    db.create_table()


def test_add_and_list():
    db.add_expense(150, "Food", "2026-10-12", "Lunch")
    rows = db.list_expenses()
    assert len(rows) == 1
    assert rows[0][1] == 150
    assert rows[0][2] == "Food"


def test_rejects_non_positive_amount():
    with pytest.raises(sqlite3.IntegrityError):
        db.add_expense(-5, "Food", "2026-10-12")


def test_update_expense():
    db.add_expense(150, "Food", "2026-10-12", "Lunch")
    assert db.update_expense(1, 180, "Food", "2026-10-12", "Lunch + juice")
    assert db.list_expenses()[0][1] == 180


def test_update_missing_id_returns_false():
    assert db.update_expense(99, 10, "Food", "2026-10-12") is False


def test_delete_expense():
    db.add_expense(150, "Food", "2026-10-12")
    assert db.delete_expense(1) is True
    assert db.list_expenses() == []
    assert db.delete_expense(1) is False


def test_monthly_total():
    db.add_expense(150, "Food", "2026-10-12")
    db.add_expense(60, "Travel", "2026-10-13")
    db.add_expense(500, "Dress", "2026-11-01")
    assert db.monthly_total("2026-10") == 210
    assert db.monthly_total("2026-09") == 0


def test_totals_by_category():
    db.add_expense(150, "Food", "2026-10-12")
    db.add_expense(200, "Food", "2026-10-14")
    db.add_expense(60, "Travel", "2026-10-13")
    assert db.totals_by_category("2026-10") == [("Food", 350), ("Travel", 60)]