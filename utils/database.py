import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent.parent / "test_data.db"


def create_database():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS users (
                                                        id INTEGER PRIMARY KEY,
                                                        username TEXT,
                                                        email TEXT
                   )
                   """)

    cursor.execute("""
        INSERT OR REPLACE INTO users (id, username, email)
        VALUES (1, 'standard_user', 'standard@example.com')
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()