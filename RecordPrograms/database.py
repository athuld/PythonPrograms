import pymysql

con = pymysql.connect(
    host="localhost", port=3306, database="db", user="root", passwd="root"
)

cursor = con.cursor()


def insert():
    sql = "insert into test values(25,'Athul',23)"
    id = int(input("Enter the id: "))
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    sql = f"insert into test values({id},'{name}',{age})"
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


while True:
    print("\n1.Insert\n2.Display\n3.Exit")
    ch = int(input("Enter the choice: "))
    if ch == 1:
        insert()
    elif ch == 2:
        display()
    else:
        break

con.close()
