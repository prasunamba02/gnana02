CREATE TABLE Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other'),
    phone VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_name VARCHAR(100),
    appointment_date DATETIME,
    reason TEXT,
    status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

CREATE TABLE Billing (
    billing_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    appointment_id INT,
    amount DECIMAL(10, 2),
    billing_date DATE,
    payment_status ENUM('Pending', 'Paid', 'Denied') DEFAULT 'Pending',
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id)
);

CREATE TABLE Claims (
    claim_id INT AUTO_INCREMENT PRIMARY KEY,
    billing_id INT,
    insurance_provider VARCHAR(100),
    claim_date DATE,
    claim_status ENUM('Filed', 'Approved', 'Denied', 'Pending') DEFAULT 'Filed',
    FOREIGN KEY (billing_id) REFERENCES Billing(billing_id)
);

CREATE TABLE LabTests (
    test_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    test_name VARCHAR(100),
    test_date DATE,
    result TEXT,
    result_status ENUM('Pending', 'Completed') DEFAULT 'Pending',
    doctor_name VARCHAR(100),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

CREATE TABLE Diagnostics (
    diagnostic_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    diagnostic_type VARCHAR(100),
    report_date DATE,
    findings TEXT,
    doctor_name VARCHAR(100),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);
