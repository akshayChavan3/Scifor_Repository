# Main program
if __name__ == "__main__":

    class Hospital:
        def __init__(self, name):
            self.name = name


    # Main program
    if __name__ == "__main__":
        hospital_name = "The Rainbow Hospital"  # Define the hospital name
        hospital = Hospital(hospital_name)


    class Patient:
        def __init__(self, patient_id, name, disease, doctor_incharge):

            self.patient_id = patient_id
            self.name = name
            self.disease = disease
            self.doctor_incharge = doctor_incharge


    class Hospital:
        def __init__(self, hospital_name):
            self.hospital_name = hospital_name
            self.patients = []


    while True:
        print("\nMenu:")
        print("1. Admit Patient")
        print("2. Get Patient Details")
        print("3. Show All Patients")
        print("4. Discharge Patient")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nEnter Patient details:")
            patient_id = int(input("Enter Patient ID: "))
            name = input("Enter Patient Name: ")
            disease = input("Enter Disease: ")
            doctor_incharge = input("Enter Doctor in Charge: ")
            hospital.admit_patient( patient_id = 2322, patient= 'mahesh', disease = 'fever', doctor_incharge = 'Robert')
        elif choice == "2":
            print("\nSearch Patient details:")
            identifier = input("Enter Patient ID, Name, Disease, or Doctor in Charge: ")
            hospital.admit_patient,get_patient(identifier)
        elif choice == "3":
            hospital.admit_patient, show_all_patients()
        elif choice == "4":
            print("\nDischarge Patient:")
            identifier = input("Enter Patient ID, Name, Disease, or Doctor in Charge to discharge: ")
            hospital.admit_patient, discharge_patient(identifier)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")




