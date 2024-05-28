# db.py
import sqlite3


def connect_to_database():
    # Connect to the SQLite database (replace 'your_database.db' with your database file path)
    conn = sqlite3.connect("prod.db")
    return conn


def fetch_data_from_db():
    conn = connect_to_database()
    cursor = conn.cursor()
    # Assuming you have a table named 'your_table' with an 'integer_data' column
    cursor.execute("SELECT price FROM products")
    data = cursor.fetchone()
    conn.close()
    return data[0] if data else None


def double_data():
    data = fetch_data_from_db()
    if data is not None:
        # Process the data and return the result (multiply by 2 in this example)
        result = data * 2
        return result
    else:
        return None


if __name__ == "__main__":

    sql = "INSERT INTO products VALUES ( :price)"
    data = {"price": 200}

    DB = "prod.db"

    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        print("Successfully Connected to SQLite")

        #  count = cursor.execute(sql)
        conn.execute(sql, data)
        conn.commit()
        print(
            "Record inserted successfully into SqliteDb_developers table ",
            cursor.rowcount,
        )
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print("Printing detailed SQLite exception traceback: ")

    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")
