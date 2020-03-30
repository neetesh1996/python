# import sqlite3
import mysql.connector

con=mysql.connector.connect(
    database ="pydb",
    user = "root" ,
    password="" ,
    host="localhost",
    port="3306" )
def create_table():
    conn=mysql.connector.connect(
    database ="pydb",
    user = "root" ,
    password="" ,
    host="localhost",
    port="3306" )
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store1 (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
def insert(item,quantity,price):
    conn=con
    cur=conn.cursor()
    cur.execute("INSERT INTO store1 VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()
  
# insert("Plane Height", 3, 5.6)  
 
 

    

def view():
    # conn=mysql.connector.connect("lite.db")
    conn=mysql.connector.connect(
    database ="pydb",
    user = "root" ,
    password="" ,
    host="localhost",
    port="3306" )
    cur=conn.cursor()
    cur.execute("SELECT * FROM store1")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=con
    cur=conn.cursor()
    cur.execute("DELETE  FROM store1 WHERE item=%s",(item,))
    conn.commit()
    conn.close()  

def update(quantity,price,item):
    conn=con
    cur=conn.cursor()
    cur.execute("UPDATE  store1  SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()        

create_table()
# insert("Apple",14,80)  
# delete("Apple")
update(56,34,"Apple")
print(view())  