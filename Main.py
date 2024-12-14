import os
from datetime import datetime

PACKAGE_FILE = "packages.txt"
REPORT_FILE = "admin_reports.txt"
USER_REPORT_FILE_PREFIX = "reports.txt"
USER_DATA = "users.txt"

def main_menu():
    while True:
        print("\nPackage Management System")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            admin_login()
        elif choice == '2':
            user_login()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

def admin_login():
    print("\nAdmin Login")
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin":
        print("Admin login successful.")
        admin_dashboard()
    else:
        print("Invalid admin credentials.")

def admin_dashboard():
    while True:
        print("\nAdmin Dashboard")
        print("1. View Reports")
        print("2. Manage Deliveries")
        print("3. Register Package")
        print("4. Logout")

        choice = input("Choose an option: ")

        if choice == '1':
            view_reports()
        elif choice == '2':
            manage_deliveries()
        elif choice == '3':
            register_package()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def view_reports():
    print("\nViewing Reports...")
    try:
        with open(REPORT_FILE, "r") as file:
            reports = file.readlines()
            if reports:
                print("Recent Activity:")
                for report in reports:
                    print(report.strip())
            else:
                print("No reports available.")
    except IOError:
        print("Error reading reports file.")

def manage_deliveries():
    print("\nManaging Deliveries...")
    packages = get_packages()

    if not packages:
        print("No packages available.")
        return

    print("Select a package to manage:")
    for i, pkg in enumerate(packages):
        print(f"{i + 1}. Package UID: {pkg[0]} - {pkg[2]}")

    try:
        package_choice = int(input("Enter the number of the package you want to manage: ")) - 1
        selected_package = packages[package_choice]
        package_uid = selected_package[0]
        print(f"\nManaging Package: {package_uid} - {selected_package[2]}")

        print("1. Pick up Package")
        print("2. Delete Package")
        print("3. Cancel")
        action_choice = input("Choose an action: ")

        if action_choice == '1':
            pick_up_package(package_uid, selected_package[1])
        elif action_choice == '2':
            delete_package(package_uid)
        elif action_choice == '3':
            return
        else:
            print("Invalid choice.")
    except (ValueError, IndexError):
        print("Invalid selection.")

def get_packages():
    packages = []
    try:
        with open(PACKAGE_FILE, "r") as file:
            for line in file:
                packages.append(line.strip().split(","))
    except IOError:
        print("Error reading package file.")
    return packages

def pick_up_package(package_uid, student_id):
    picker_id = input("Enter Picker ID: ")
    timestamp = get_current_datetime()
    report = f"{package_uid},{student_id},{picker_id},{timestamp}"
    
    save_report_to_file(REPORT_FILE, report)
    save_user_report(student_id, package_uid, picker_id, timestamp)
    delete_package(package_uid)

    print(f"Package {package_uid} picked up successfully.")

def delete_package(package_uid):
    try:
        with open(PACKAGE_FILE, "r") as file:
            lines = file.readlines()

        with open(PACKAGE_FILE, "w") as file:
            for line in lines:
                if not line.startswith(package_uid):
                    file.write(line)

        timestamp = get_current_datetime()
        report = f"Package {package_uid} was deleted at {timestamp}"
        save_report_to_file(REPORT_FILE, report)

        print(f"Package {package_uid} deleted successfully.")
    except IOError:
        print("Error deleting package.")

def save_report_to_file(file_name, report):
    try:
        with open(file_name, "a") as file:
            file.write(report + "\n")
    except IOError:
        print("Error saving report.")

def save_user_report(owner_student_id, package_uid, picker_id, timestamp):
    user_report_file = USER_REPORT_FILE_PREFIX + owner_student_id + ".txt"
    report = f"{package_uid},{owner_student_id},{picker_id},{timestamp}"
    save_report_to_file(user_report_file, report)

def register_package():
    package_uid = input("Enter Package UID: ")
    student_id = input("Enter Student ID: ").upper()
    description = input("Enter Package Description: ")
    arrival_date = get_current_datetime()

    if package_uid and student_id and description:
        try:
            with open(PACKAGE_FILE, "a") as file:
                file.write(f"{package_uid},{student_id},{description},Pending,{arrival_date}\n")
            print(f"Package {package_uid} registered successfully.")
        except IOError:
            print("Error registering package.")
    else:
        print("Please fill in all fields.")

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def user_login():
    print("\nUser Login")
    college_id = input("College ID: ").upper()
    password = input("Password: ")

    user_data = authenticate_user(college_id, password)
    if user_data:
        print(f"Login successful. Welcome {user_data['name']}!")
        user_dashboard(user_data['name'], college_id)
    else:
        print("Invalid College ID or Password.")

def authenticate_user(college_id, password):
    try:
        with open(USER_DATA, "r") as file:
            for line in file:
                name, stored_college_id, stored_password = line.strip().split(',')
                if stored_college_id == college_id and stored_password == password:
                    return {'name': name, 'college_id': stored_college_id, 'password': stored_password}
    except IOError:
        print("Error reading user file.")
    return None

def user_dashboard(user_name, college_id):
    while True:
        print(f"\nWelcome {user_name}!")
        print("1. Track Order")
        print("2. View Reports")
        print("3. Logout")

        choice = input("Choose an option: ")

        if choice == '1':
            track_order(college_id)
        elif choice == '2':
            reports(user_name)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

def track_order(college_id):
    print("Tracking your order...\n")
    
    try:
        with open(PACKAGE_FILE, "r") as file:
            found_packages = False
            for line in file:
                package_details = line.strip().split(",")
                
                if len(package_details) >= 5:
                    package_id = package_details[0].strip()
                    student_id = package_details[1].strip()
                    description = package_details[2].strip()
                    status = package_details[3].strip()
                    date_time = package_details[4].strip()
                    
                    if student_id == college_id and status == "Pending":
                        print(f"Package ID: {package_id}")
                        print(f"Package Description: {description}")
                        print(f"Status: {status}")
                        print(f"Date and Time: {date_time}\n")
                        found_packages = True
            
            if not found_packages:
                print("No pending packages found for your ID.")
    
    except IOError:
        print("Error reading the package status file. Please try again later.")

def reports(user_name):
    print(f"\nViewing reports for {user_name}...")
    try:
        with open(REPORT_FILE, "r") as file:
            found = False
            for line in file:
                report_details = line.strip().split(',')
                if report_details[1] == user_name:
                    print(f"Package ID: {report_details[0]}")
                    print(f"Owner ID: {report_details[1]}")
                    print(f"Picker ID: {report_details[2]}")
                    print(f"Date: {report_details[3]}")
                    found = True
            if not found:
                print("No reports found.")
    except IOError:
        print("Error reading reports file.")

if __name__ == "__main__":
    main_menu()
