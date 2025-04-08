import sqlite3

## Connect to sqllite database
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record, create tables, retreive data
cursor = connection.cursor()

## create a table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

## Insert records
cursor.execute('''Insert Into STUDENT values('Tanuj', 'Data Science', 'A', 95)''')
cursor.execute('''Insert Into STUDENT values('Atharva', 'Data Science', 'B', 92)''')
cursor.execute('''Insert Into STUDENT values('Aaryan', 'Data Science', 'A', 93)''')
cursor.execute('''Insert Into STUDENT values('Harish', 'DEVOPS', 'A', 94)''')
cursor.execute('''Insert Into STUDENT values('Urvi', 'DEVOPS', 'A', 91)''')

## DISPLAY
print("The inserted records are:")

data=cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)

## close the connection
connection.commit()
connection.close()