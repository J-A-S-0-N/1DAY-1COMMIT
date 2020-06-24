import sqlite3

conn = sqlite3.connect("employee.db")

c = conn.cursor()

#c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#            pay integer
#            )""")

c.execute("INSERT INTO test VALUES ('jason', 'korea' , 10000)")

c.execute("SELECT * FROM test WHERE last = 'korea'")

print(c.fetchall())
conn.commit()

conn.close()
