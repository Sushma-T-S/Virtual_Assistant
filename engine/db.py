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