import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "azerty123",
    database = "python"
)

mydb.autocommit = True

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE students( name VARCHAR(255), age INTEGER(3))")

# mycursor.execute("INSERT INTO students VALUES('HASSANE', '35')")

mycursor.execute("SELECT * FROM students")

for student in mycursor:
    print(student)

