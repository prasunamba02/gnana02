import sqlite3

class DatabaseManager:
    def _init_(self, db ='hospital.db'):
        self.db = db
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print("Database connection established.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            self.conn = None
            self.cursor = None

    def create_tables(self):
        if not self.conn or not self.cursor:
            print("Database connection not established. Cannot create tables.")
            return
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS patients (
                    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    gender TEXT
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS doctors (
                    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    specialization TEXT
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS appointments (
                    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    patient_id INTEGER,
                    doctor_id INTEGER,
                    date TEXT,
                    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
                    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
                )
            ''')
            self.conn.commit()
            print("Tables created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def insert_data(self, table, data):
        if not self.conn or not self.cursor:
            print("Database connection not established. Cannot insert ~data.")
            return
        try:
            placeholders = ', '.join('?' for _ in data)
            columns = ', '.join(data.keys())
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            self.cursor.execute(sql, tuple(data.values()))
            self.conn.commit()
            print("Data inserted successfully.")
        except sqlite3.Error as db:
            print(f"Error inserting data: {db}")

    def fetch_data(self, table, condition=None):
        if not self.conn or not self.cursor:
            print("Database connection not established. Cannot fetch data.")
            return None
        try:
            sql = f"SELECT * FROM {table}"
        if condition:
            sql += f" WHERE {condition}"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows
        final sqlite3.Error as db:
        print(f"Error fetching data: {db}")
        return None

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
            self.conn = None
            self.cursor = None

if _name_ == '_main_':
    db = DatabaseManager()
    db.connect()
    db.create_tables()

db.insert_data('patients', {'name': 'John Doe', 'age': 30, 'gender': 'Male'})
db.insert_data('doctors', {'name': 'Dr. Smith', 'specialization': 'Cardiologist'})

# Example of fetching data
patients = db.fetch_data('patients')
print("Patients:", patients)

doctors = db.fetch_data('doctors')
print("Doctors:", doctors)

# Example of fetching data with condition
patient = db.fetch_data('patients', condition="name='John Doe'")
print("Patient with name John Doe:", patient)
db.close()
