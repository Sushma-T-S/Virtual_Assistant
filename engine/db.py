import csv
import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100),url VARCHAR(100))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'chatgpt',' https://chat.openai.com/')"
# cursor.execute(query)
# conn.commit()
# query = "INSERT INTO web_command VALUES (null,'chatgpt',' https://chatgpt.com/')"
# cursor.execute(query)
# conn.commit()
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) null)''')
#Specify the column indices you want to import (0-based index)
#Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 20]
# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# conn.commit()
# conn.close()


# Adding single contacts

# query = "INSERT INTO contacts VALUES(null, 'vaishu', '9686335995', 'null')"
# cursor.execute(query)
# conn.commit()

#searching the number

# query = 'jeeshan'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])