import mysql.connector

try:
    my_connection = mysql.connector.connect(
        host="localhost",
        user="userland",
        password="emma"
    )
    my_cursor = my_connection.cursor()
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print("Connection failed")
finally:
    if my_cursor:
        my_cursor.close()
    if my_connection:
        my_connection.close()
