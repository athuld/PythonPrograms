import MySQLdb

con = MySQLdb.connect(
    host="localhost", port=3306, database="db", user="root", passwd="root"
)

cursor = con.cursor()

def delete():
    id = int(input("Enter the id: "))
    sql = "delete from test where id={}".format(id)
    try:
        cursor.execute(sql)
        con.commit()
        print("Deleted")
    except:
        con.rollback()

def update():
    id = int(input("Enter the id: "))
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    sql = "update test set name='{}',age={} where id={}".format(name,age,id)
    try:
        cursor.execute(sql)
        con.commit()
        print("Data Updated")
    except:
        con.rollback()

def insert():
    id = int(input("Enter the id: "))
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    sql = "insert into test values({},'{}',{})".format(id,name,age)
    try:
        cursor.execute(sql)
        con.commit()
        print("Data inserted")
    except:
        con.rollback()


def display():
    sql = "select * from test"
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
    except:
        print("Unable to fetch data")

def create_table():
    sql="create table test(id int,name varchar(30),age int)"
    try:
        cursor.execute(sql)
        con.commit()
        print("Table created")
    except:
        con.rollback()

while True:
    print("\n1.Insert\n2.Display\n3.Delete\n4.Update\n5.Create Table\n6.Exit")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        insert()
    elif ch == 2:
        display()
    elif ch == 3:
        delete()
    elif ch == 4:
        update()
    elif ch == 5:
        create_table()
    else:
        break

con.close()
