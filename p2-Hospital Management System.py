from datetime import datetime

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Patient(Person):
    def __init__(self, patient_id, name, age, gender, illness):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.illness = illness
    
    def __str__(self):
        return f"[Patient] {self.name}. Age: {self.age}, Illness: {self.illness}"
    
class Doctor(Person):
    def __init__(self, doctor_id, name, age, gender, specialization):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def __str__(self):
        return f"[Doctor] Dr. {self.name}. Age: {self.age}, Specialization: {self.specialization}"
    
class Appointment:
    def __init__(self, appointment_id, patient, doctor, date_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time
    def __str__(self):
        return (f"Appointment #{self.appointment_id}\n"
                f"Date/Time: {self.date_time}\n"
                f"Doctor: {self.doctor.name}\n"
                f"Patient: {self.patient.name}")

class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []
    
    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} added to the hospital.") 
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor {doctor.name} added to the hospital.")
    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)
        print(f"Appointment scheduled for {appointment.patient.name} with Dr. {appointment.doctor.name} on {appointment.date_time}.")
    def show_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
            return
        for appointment in self.appointments:
            print(appointment)
    def show_patients(self):
        if not self.patients:
            print("No patients in the hospital.")
            return
        for patient in self.patients:
            print(patient)
    def show_doctors(self):
        if not self.doctors:
            print("No doctors in the hospital.")
            return
        for doctor in self.doctors:
            print(doctor)


hospital = Hospital("Piyush HealthCare")
# Add Doctors
doc1 = Doctor(1, "AMit SHarma", 45, "Male", "Cardiology")
doc2 = Doctor(2, "Priya", 38,"Female", "Neurology")
hospital.add_doctor(doc1)
hospital.add_doctor(doc2)

# Add Patients
pat1 = Patient(101, "Ravi Kumar", 30, "Male", "Chest Pain")
pat2 = Patient(102, "Anjali Mehta", 25, "Female", "Headache")
hospital.add_patient(pat1)
hospital.add_patient(pat2)

# Schedule Appointments
app1 = Appointment(1001, pat1, doc1, datetime(2025, 7, 2, 11, 0))
app2 = Appointment(1002, pat2, doc2, datetime(2025, 7, 3, 14, 30))
hospital.schedule_appointment(app1)
hospital.schedule_appointment(app2)

# Show all records
hospital.show_doctors()
hospital.show_patients()
hospital.show_appointments()