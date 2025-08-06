import mysql.connector
def  connect():
    Conn= mysql.connector.connect(
        host="localhost",
        user="root",
        password="prasuna@021104",
        database="Hospital_management"
    )
    return Conn
if (connect()):
    print("connection establish")
else:
    print("connection failed")
