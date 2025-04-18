import mysql.connector

conn = mysql.connector.connect(
    host="localhost",  # Или IP сервера
    user="root",
    password=""
)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS fitness_db")
cursor.execute("USE fitness_db")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS steps (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        steps INT NOT NULL
    )
""")

print(" The database and table have been created!")

cursor.close()
conn.close()
