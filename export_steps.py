import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fitness_db"
)

query = "SELECT * FROM steps"
df = pd.read_sql(query, conn)

df.to_csv("steps_data.csv", index=False, encoding="utf-8")
print("The data is saved in steps_data.csv")

df.to_excel("steps_data.xlsx", index=False, engine="openpyxl")
print("The data is saved in steps_data.xlsx")


conn.close()
