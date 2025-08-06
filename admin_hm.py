from user import connect
def signup():
    conn=connect()
    cursor=conn.cursor()
    username=input("enter your username:")
    password=input("enter your password:")
    result=cursor.fetchone()
    if result:
        print("username already exists.try.logging in.")
    else:
        cursor.execute("insert into users(username,password)")
        conn.commit()
        print("singup successfully")
    cursor.close()  
    conn.close

def log_in():
    conn=connect()
    cursor=conn.cursor()
    username=input("enter your username:")
    password=input("enter your password:")
    if username == "username" and password == "password":
        print("into into  login successful.")
        return True
    else:
        print("insert into login is not succeessfull")
        return False
    
    

