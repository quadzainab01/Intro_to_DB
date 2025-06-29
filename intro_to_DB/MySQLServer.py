import mysql.connector

from mysql.connector import errorcode

def create_database():
    try:
        connection = mysql.connector.connect(
            host="db4free.net",
            port=3306,
            user="quadzainab01",
            password="Allahisgreat"
        )

        cursor = connection.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid username or password.")
        else:
            print(f"Connection Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()

