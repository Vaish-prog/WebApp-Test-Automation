import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent.parent / "test_data.db"


def test_user_data():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT username, email FROM users WHERE id = 1"
    )

    user = cursor.fetchone()

    assert user is not None
    assert user[0] == "standard_user"
    assert user[1] == "standard@example.com"

    connection.close()