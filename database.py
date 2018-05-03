import sqlite3
conn = sqlite3.connect('rishi.db')
c = conn.cursor()
def createTable():
    c.execute("CREATE TABLE student(RollNumber VARCHAR,Name VARCHAR,Marks REAL)")

def insertData():
    c.execute("INSERT INTO student values(1,'Ram',10)")
    c.execute("INSERT INTO student values(2,'Raju',15)")
    c.execute("INSERT INTO student values(3,'Rita',18)")
    c.execute("INSERT INTO student values(4,'Renu',19)")
    c.execute("INSERT INTO student values(5,'Rohit',99)")

#insertData()
def read_from_database():
    sql = "SELECT * FROM student"
    for row in c.execute(sql):
        print(row)
        print(row[0])
        
read_from_database()

conn.close()
