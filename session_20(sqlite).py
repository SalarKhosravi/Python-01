# sqlite3 and python
# https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial

import sqlite3
import os

# Function to create a database (if it doesn't exist)
def create_database(db_name):
    if not os.path.exists(db_name):  # Check if the database file exists
        conn = sqlite3.connect(db_name)  # Create a new database file
        conn.close()
        print(f"Database '{db_name}' created.")
    else:
        print(f"Database '{db_name}' already exists.")

# Function to create the 'user' table if it doesn't already exist
def create_table(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()
    print("Table 'user' created (if not already existing).")
    conn.close()

# Function to insert data into the 'user' table
def insert_user(db_name, name, age):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print(f"User '{name}' with age {age} inserted into the table.")
    conn.close()

# Function to read all records from the 'user' table
def read_all_records(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    print("All records from 'user' table:")
    for row in rows:
        print(row)
    conn.close()

# Function to delete a record where id = 3
def delete_record(db_name, record_id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user WHERE id = ?", (record_id,))
    conn.commit()
    print(f"Record with id = {record_id} deleted.")
    conn.close()

# Function to update a record where id = 2
def update_record(db_name, record_id, new_name, new_age):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET name = ?, age = ? WHERE id = ?", (new_name, new_age, record_id))
    conn.commit()
    print(f"Record with id = {record_id} updated to name '{new_name}' and age {new_age}.")
    conn.close()

# Example usage
db_name = 'example.db'

# Create database if it doesn't exist
create_database(db_name)

# Create the 'user' table if it doesn't exist
create_table(db_name)

# Insert some data into the 'user' table
insert_user(db_name, 'Alice', 30)
insert_user(db_name, 'Bob', 25)
insert_user(db_name, 'Charlie', 35)

# Read all records
read_all_records(db_name)

# Delete the record where id = 3
delete_record(db_name, 3)

# Update the record where id = 2
update_record(db_name, 2, 'Robert', 28)

# Read all records again after deletion and update
read_all_records(db_name)











# my sql
import mysql.connector
from mysql.connector import Error

# Function to create a database (if it doesn't exist)
def create_database(db_name, connection):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        connection.commit()
        print(f"Database '{db_name}' created or already exists.")
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        cursor.close()

# Function to create the 'user' table if it doesn't already exist
def create_table(db_name, connection):
    cursor = connection.cursor()
    cursor.execute(f"USE {db_name}")  # Switch to the specific database
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT NOT NULL
            )
        ''')
        connection.commit()
        print("Table 'user' created (if not already existing).")
    except Error as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()

# Function to insert data into the 'user' table
def insert_user(db_name, connection, name, age):
    cursor = connection.cursor()
    cursor.execute(f"USE {db_name}")  # Switch to the specific database
    try:
        cursor.execute("INSERT INTO user (name, age) VALUES (%s, %s)", (name, age))
        connection.commit()
        print(f"User '{name}' with age {age} inserted into the table.")
    except Error as e:
        print(f"Error inserting user: {e}")
    finally:
        cursor.close()

# Function to read all records from the 'user' table
def read_all_records(db_name, connection):
    cursor = connection.cursor()
    cursor.execute(f"USE {db_name}")  # Switch to the specific database
    try:
        cursor.execute("SELECT * FROM user")
        rows = cursor.fetchall()
        print("All records from 'user' table:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error reading records: {e}")
    finally:
        cursor.close()

# Function to delete a record where id = 3
def delete_record(db_name, connection, record_id):
    cursor = connection.cursor()
    cursor.execute(f"USE {db_name}")  # Switch to the specific database
    try:
        cursor.execute("DELETE FROM user WHERE id = %s", (record_id,))
        connection.commit()
        print(f"Record with id = {record_id} deleted.")
    except Error as e:
        print(f"Error deleting record: {e}")
    finally:
        cursor.close()

# Function to update a record where id = 2
def update_record(db_name, connection, record_id, new_name, new_age):
    cursor = connection.cursor()
    cursor.execute(f"USE {db_name}")  # Switch to the specific database
    try:
        cursor.execute("UPDATE user SET name = %s, age = %s WHERE id = %s", (new_name, new_age, record_id))
        connection.commit()
        print(f"Record with id = {record_id} updated to name '{new_name}' and age {new_age}.")
    except Error as e:
        print(f"Error updating record: {e}")
    finally:
        cursor.close()

# Example usage
try:
    # Connect to MySQL
    connection = mysql.connector.connect(
        host='localhost',       # Replace with your MySQL server host
        user='root',            # Replace with your MySQL username
        password='password'     # Replace with your MySQL password
    )

    db_name = 'example_db'

    # Create database if it doesn't exist
    create_database(db_name, connection)

    # Create the 'user' table if it doesn't exist
    create_table(db_name, connection)

    # Insert some data into the 'user' table
    insert_user(db_name, connection, 'Alice', 30)
    insert_user(db_name, connection, 'Bob', 25)
    insert_user(db_name, connection, 'Charlie', 35)

    # Read all records
    read_all_records(db_name, connection)

    # Delete the record where id = 3
    delete_record(db_name, connection, 3)

    # Update the record where id = 2
    update_record(db_name, connection, 2, 'Robert', 28)

    # Read all records again after deletion and update
    read_all_records(db_name, connection)

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
