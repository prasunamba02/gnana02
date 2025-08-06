class Patient:
    def __init__(self, patient_id, name,date_of_birth,age, gender,contact):
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth= date_of_birth
        self.age = age
        self.gender = gender
        self.contact=contact

    def update_details(self, name=None, age=None, gender=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if gender:
            self.gender = gender

class Doctor:
    def __init__(self, doctor_id, name, speciality):
        self.doctor_id = doctor_id
        self.name = name
        self.speciality = speciality

class Appointments:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time,status):
        self.appointment_id = appointment_id
        self.patient_id= patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.status=status

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)


  
if patient=doctor:
    PRIN
