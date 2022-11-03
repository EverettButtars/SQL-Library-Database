import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

#conect to database
library = mysql.connector.connect(
    host = "localhost",
    user = "Admin",
    password = "Library",
    database = "Library"
)
cursor = library.cursor()

cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)

query = "SELECT * FROM books"
cursor.execute(query)
cursor.fetchall()
print(cursor.column_names)


query = "SELECT SUM(Volume) FROM books"

cursor.execute(query)
data = cursor.fetchall()
print("total copies of the books in library printed worldwide: " + str(int(data[0][0])))