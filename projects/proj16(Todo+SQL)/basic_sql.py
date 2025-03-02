import sqlite3

# ============== 1. Common Field Types in SQLite3 =============
# Here are the most common field types you will encounter in SQLite3:
# INTEGER: Stores integers (whole numbers).
# TEXT: Stores text (strings).
# REAL: Stores floating-point numbers.
# BLOB: Stores binary data (like images).
# NUMERIC: Stores numbers, but can also store dates and times.
# NULL: A field that allows NULL values (no value).


# =============== 2. Field Constraints ==================
# Here are some common constraints used with fields:
# PRIMARY KEY: Ensures the column is unique and cannot be NULL. Often used for identifiers.
# AUTOINCREMENT: Automatically increments an integer value for the primary key.
# NOT NULL: Ensures that a column cannot have a NULL value.
# DEFAULT: Specifies a default value for a column when no value is provided during insertion.
# UNIQUE: Ensures all values in a column are unique.
# FOREIGN KEY(user_id) REFERENCES users(id),



connection = sqlite3.connect('pet_shop.db')
cursor = connection.cursor()

# create users table
#  --------------------------------
# create_users_table_query = '''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         full_name TEXT NOT NULL,
#         email TEXT NOT NULL UNIQUE,
#         marriage_status BOOLEAN NOT NULL default FALSE,
#         password TEXT NOT NULL,
#         balance Numeric NOT NULL default 0
#     )
# '''
# cursor.execute(create_users_table_query)




# create users table
#  ----------------------------------------
# create_products_table_query = '''
#     CREATE TABLE IF NOT EXISTS products (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         price Numeric NOT NULL,
#         is_exist BOOLEAN NOT NULL default TRUE,
#         description TEXT NULL default ''
#     )
# '''
# cursor.execute(create_products_table_query)





# Create Invoices table
#  ----------------------------------------
# create_invoices_table_query = '''
#     CREATE TABLE IF NOT EXISTS invoices (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER,
#         product_id INTEGER,
#         quantity INTEGER NOT NULL,
#         total REAL NOT NULL,
#         FOREIGN KEY(user_id) REFERENCES users(id),
#         FOREIGN KEY(product_id) REFERENCES products(id)
#     )
# '''
# cursor.execute(create_invoices_table_query)





# ============ Create records (insert) ==============

# Insert into users
# cursor.execute("INSERT INTO users (full_name, email, marriage_status, password, balance) VALUES (?, ?, ?, ?, ?)", ("John Doe", "john@example.com", True, 'abc', 30))
# connection.commit()
# connection.close()


# Insert into products
# cursor.execute("INSERT INTO products (name, price, is_exist, description) VALUES (?, ?, ?, ?)", ("Laptop", 999.99, True, 'empty'))
# connection.commit()
# connection.close()


# Insert into invoices (assuming user_id=1 and product_id=1 exist)
# cursor.execute("INSERT INTO invoices (user_id, product_id, quantity, total) VALUES (?, ?, ?, ?)", (1, 1, 3, 120))
# connection.commit()
# connection.close()





# Insert multiple value to user table
# data = [
#     ("Ali Akbari", 'ali@gmail.com', '123'),
#     ("Sara Ahadi", 'sara@gmail.com', '321'),
#     ("Ben Mira", 'ben@gmail.com', '333'),
#     ("Saeed Sobhan", 'saeed@gmail.com', '4444'),
#     ("Maryam Imani", 'maryam@gmail.com', '1111'),
#
# ]
#
# cursor.executemany("INSERT INTO users (full_name, email, password) VALUES(?, ?, ?)", data)
# connection.commit()
# connection.close()


# Insert multiple value to products table
# data = [
#     ("Dell", 123),
#     ("Iphone 16", 321),
#     ("Samsung s20", 333),
#     ("LG TV", 4444),
#     ("Macbook", 1111),
# ]
#
# cursor.executemany("INSERT INTO products (name, price) VALUES(?, ?)", data)
# connection.commit()
# connection.close()


# Insert multiple value to invoice table
# data = [
#     (1, 2, 3, 110),
#     (2, 3, 1, 120),
#     (2, 4, 1, 300),
#     (2, 5, 2, 200),
#     (4, 1, 1, 150),
#     (4, 3, 2, 120),
#     (2, 4, 5, 270),
# ]
#
# cursor.executemany("INSERT INTO invoices (user_id, product_id, quantity, total) VALUES(?, ?, ?, ?)", data)
# connection.commit()
# connection.close()



# ============= Read sqlite =============

# Select all users
# cursor.execute("SELECT * FROM users")
# users = cursor.fetchall()
# for user in users:
#     print(user)



# Select specific user
# cursor.execute("SELECT * FROM users WHERE id = 3")
# user = cursor.fetchone()
# print(user)



# Join tables (e.g., invoices with users and products)
# cursor.execute('''
#         SELECT users.full_name, products.name, invoices.quantity, invoices.total
#          FROM invoices
#          JOIN users ON invoices.user_id = users.id
#          JOIN products ON invoices.product_id = products.id
#      '''
# )
#
#
# invoices = cursor.fetchall()
# print('\n\ndata fetch from join')
# print('-----------------------------------')
# for invoice in invoices:
#     print(invoice)
#
# print('\n\n\ndata fetch from join as a text')
# print('-----------------------------------')
# for invoice in invoices:
#     print(f'{invoice[0]} has bought {invoice[2]} of {invoice[1]} for {invoice[3]} Euros')


