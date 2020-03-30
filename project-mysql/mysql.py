import mysql.connector

con = mysql.connector.connect(
user ="root",
password ="",
host ="localhost",
database="pydb"
)

cursor =con.cursor()

query = cursor.execute("SLECT * FROM Dictionary")