from db import connect
def admin():
    conn=connect()
    cursor=conn.cursor()
    print("""~\nAdmin menu:
          1.add student
          2.update student details
          3.reset student password
          4.add marks
          5.update marks,
          6.view all students
          7.update timetable
          8.logout""")
    ch=int(input("enter your choice(1-8):"))
    if ch==1:
        add_student()            
    elif ch==2:
        update_student()
    elif ch==3:
        reset_student_password()
    elif ch==4:
        add_marks()
    elif ch==5:
        update_marks()
    elif ch==6:
        view_all_students()
    elif ch==7:
        update_timetable()
    elif ch==8:
        logout()
    else:
        print("invalid choice.please try again")
def  add_student():
    conn=connect()
    cursor=conn.cursor()
    roll_no=input("enter roll no:")
    name=input("enter name:")
    class_name=input("enter class:")
    section=input("enter section:")
    password="password default"
    email=input("enter emails:")
    query="insert into students(roll_no,name,class,section,password,email)values(%s,%s,%s,%s,%s,%s)"
    values=(roll_no,name,class_name,section,password,email)
    cursor.execute(query,values)
    conn.commit()
    print("Added successfully")
def update_student():
    conn=connect()
    cursor=conn.cursor()
    roll_no=input("enter roll no of student to update:")
    name=input("enter new name:")
    class_name=input("enter new class:")
    section=input("enter new section:")
    email=input("enter new email:")
    query="update students SET name=%s,class=%s,section=%s,email=%s where roll_no=%s"
    values=(name,class_name,section,email,roll_no)
    cursor.execute(query,values)
    conn.commit()
    print("updated successfully")
def reset_student_password():
    pass
def add_marks():
    conn=connect()
    cursor=conn.cursor()
    roll_no=input("enter roll no:")
    subject=input("enter your subject:")
    marks=input("enter your marks:")
    query="insert into marks6(roll_no,subject,marks)values(%s,%s,%s)"
    values=(roll_no,subject,marks)
    cursor.execute(query,values)
    conn.commit()
    print("marks added successfully")
def update_marks():
    conn=connect()
    cursor=conn.cursor()
    roll_no=input("enter roll no of student to update:")
    subject=input("enter subject:")
    marks=input("enter marks:")
    query="update marks set marks=%s where roll_no=%s"
    values=(marks,roll_no,subject)
    cursor.execute(query,values)
    conn.commit
def view_all_students():
    conn=connect()
    cursor=conn.cursor()
    query="select * from students"
    cursor.execute(query)
    results=cursor.fetchall()
    for row in results:
        print(row)
def update_timetable():
    pass
def logout():
    print("logging out.....")
    return

admin()


