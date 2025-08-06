from user import connect
def admin():
    conn=connect()
    cursor=conn.cursor()
    print("""\nAdmin menu:
          1.log in
          2.add patient
          3.update patient
          4.add doctor
          5.udate doctor
          6.view patient
          7.log out""")
    ch=int(input("enter your choices(1-7):"))

    if ch==1: 
        log_in()
    elif ch==2:
        add_patient()
    elif ch==3:
        update_patient()
    elif ch==4:
        add_doctor()
    elif ch==5:
        update_doctor()
    elif ch==6:
        view_patients()
    elif ch==7:
        logout()
    else:
        print("invalid choices")
def log_in():
    pass
def add_patient():
    conn=connect()
    cursor=conn.cursor()
    patient_id=input("enter patient id:")
    name=input("enter patient name:")
    gender=input("enter patient gender:")
    phone=input("enter patient phone number:")
    email=input("enter email:")
    address=input("enter address:")
    query="INSERT INTO patient(patient_id,name,gender,phone,email,address)VALUES (%s, %s, %s, %s, %s,%s)"
    values=(patient_id,name,gender,phone,email,address)
    cursor.execute(query,values)
    conn.commit()
    print("added patient successfully")
def update_patient():
    conn=connect()
    cursor=conn.cursor()
    name=input("enter new patient name:")
    gender=input("enter new patient gender:")
    phone=input("enter new patient phone number:")
    email=input("enter new email:")
    address=input("enter new address:")
    query="update patient set name=%s,gender=%s,phone=%s,email=%s,address=%s where patient_id=%s"
    values=(name,gender,phone,email,address)
    cursor.execute(query,values)
    conn.commit()
    print("updated patient successfully")
def add_doctor():
    conn=connect()
    cursor=conn.cursor()
    doctor_id=input("enter doctor id:")
    doctor_name=input("enter doctor name:")
    age=input("enter doctor age:")
    specialization=input("enter doctor specialiation:")
    query=("insert into doctor(doctor_id,doctor_name,age,specialization)values(%s,%s,%s,%s)")
    values=(doctor_id,doctor_name,age,specialization)
    cursor.execute(query,values)
    conn.commit()
    print("added doctor successfully")
def update_doctor():
    conn=connect()
    cursor=conn.cursor()
    doctor_id=input("enter new doctor id:")
    doctor_name=input("enter new doctor name:")
    specialization=input("enter doctor specialiation:")
    query=("update doctor set doctor_id=%s,doctor_name=%s,specialization=%s where doctor_id=%s")
    values=(doctor_id,doctor_name,specialization)
    cursor.execute(query,values)
    conn.commit()
    print("updated doctor successfully")
def view_patients():
    conn=connect()
    cursor=conn.cursor()
    query="select * from patient"
    cursor.execute(query)
    results=cursor.fetchall()
    for row in results:
        print(row)
def logout():
    print("logging out.....")
    return



admin()  

