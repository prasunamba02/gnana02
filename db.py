import mysql.connector
def connection():
    Connect= mysql.connector.connect(
        host="localhost",
        user="root",
        password="prasuna@021104",
        database="student_management"
    )
    return Connect
if (connection()):
    print("connection establish")
else:
    print("connection failed")