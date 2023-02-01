import sqlite3

conn = sqlite3.connect("lunch.db")
c = conn.cursor()
c.execute("""CREATE TABLE meals(sandwich TEXT, fruit TEXT, tableNum INT)""")
sandwich = "ham"
fruit = "apple"
tableNum = 22
c.execute("""INSERT INTO meals VALUES(?,?,?)""",(sandwich,fruit,tableNum))
conn.commit()
#c.execute("""DROP TABLE meals""")
c.execute("""SELECT * FROM meals""")
results = c.fetchall()
print(results)
