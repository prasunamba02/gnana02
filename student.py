from db import connect
def student_menu(roll_no):
    while True:
        print("""\nStudent menu
              1. view details
              2.view marks
              3.view timetable
              4.logout""")
        choice=input("enter choice:")
        if choice == '1':
            view_details(roll_no)
        elif choice == '2':
            view_marks(roll_no)
        elif choice == '3':
            view_timetable(roll_no)
        elif choice == '4':
            print("logging out....")
            break
        else:
            print("invalid choices.")
def view_details(roll_no):
    conn=connect()
    cur=conn.cursor()
    cur.execute("select * from students where roll_no=%s",(roll,))
    print("students details:")
    print(cur.fetchone())
    con.close()
def view_marks(roll_no):
    conn=connect()
    cur=conn.cursor()
    cur.execute("select subject,marks from marks where roll_no=%s",(roll,))
    for row in cur.fetchall():
        print(row)
student_menu(3004)