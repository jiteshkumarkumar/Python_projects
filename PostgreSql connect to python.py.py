# Connecting to a PostgreSQL from python
import psycopg2
conn = psycopg2.connect(dbname="postgres",user="postgres",password="5432",host="localhost",port="5432")
# print("Successfully connected.")

# creating a databse and a table
# cursor = conn.cursor()
# cursor.execute('''create table students_dt(name text, ID int, Age int);''')
# #print("Table successfully created")
# conn.commit()
# conn.close()

#insert data into the table
def data():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="5432",host="localhost",port="5432")
    cursor = conn.cursor()
    cursor.execute("""insert into students_dt(name,ID,Age)values('Nikil',2,22);""")
    conn.commit()
    cursor.close()
    conn.close()
    print("Values are successfully insert into table.")

# Extract All value from table.
def extract():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="5432",host="localhost",port="5432")
    cursor = conn.cursor()
    cursor.execute("""select * from students_dt where name='Nikil';""")
    print(cursor.fetchall())  # need to use this function to fetch all value from the table.
    conn.commit()
    cursor.close()
    conn.close()
    print("Extracted successfully.")
    
extract()

# Taking the inputs from users

def users():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="5432",host="localhost",port="5432")
    cursor= conn.cursor()

    name = input("Enter name: ")
    ID = input("Enter ID: ")
    Age= input("Enter Age: ")

    query = "INSERT INTO students_dt (Name, ID, Age) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, ID, Age))

    conn.commit()
    print("Data successfully added.")
    cursor.close()
    conn.close()

users()      