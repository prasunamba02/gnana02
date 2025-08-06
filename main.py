from dp import connection
connect=connection()
if connect:
    print("connection establish successfully")
else:
    print("connection failed")
def insert_data():
    roll_no=int(input("enter your number:"))
    name=input("enter name:")
    branch=input("enter branch:")
    cursor=connect.cursor()
    query="insert into student1(roll_no,name,branch) values(%s,%s,%s)"
    values=(roll_no,name,branch)
    cursor.execute(query,values)
    connect.commit()
    print("data inserted successfully")
def fetch_data():
    cursor=connect.cursor()
    query="select * from student1"
    results=cursor.fetchall()
    for row in results:
        print(row)
def update_data():
    roll_no=int(input("enter your number:"))
    name=input("enter name:")
    branch=input("enter branch:")
    cursor=connect.cursor()
    query="update studeset name=%s,branch=%s where roll_no"
    values=(name,branch,roll_no)
    cursor.execute(query,values)
    connect.commit()
    print("updated successfully")
print("1,insert data")
print("2,fetch data")
print("3,update data")
print("enter 4 to exit")
while True:
    choice=int(input("enter your choice(1-4):"))
    if choice==1:
        insert_data()
    elif choice==2:
        fetch_data()
    elif choice==3:
        update_data()
    elif choice==4:
        print("exiting....")
        break


