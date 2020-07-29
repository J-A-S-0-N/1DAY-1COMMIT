import sqlite3 
from schedule import Schedule

conn = sqlite3.connect("schedule.db") 

c = conn.cursor()

#c.execute("""CREATE TABLE schedule(
#            name text,
#            time_hour integer,
#            what_it_will_print text
#            )""")

#c.execute("INSERT INTO schedule VALUES ('TEST', 10, 'TEST')")


#mysql.connector.connect(host='localhost', 
#                        database='schedule', 
#                        user='root', 
#                        password='Jason671404') 


def newschedule(time, name, what_it_will_print):
    newschedule = Schedule(time, name, what_it_will_print)

def printall():
    c.execute("SELECT * FROM schedule")
    print(c.fetchall())
    conn.commit()

def deleteschedule(row):
    pass

conn.close()