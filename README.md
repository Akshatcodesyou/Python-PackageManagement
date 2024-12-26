# Package Management System

This **Package Management System** allows admins to manage packages, view reports, and register packages for delivery. Users can log in with their college IDs to track and view reports related to their packages. Admins have access to a dashboard to manage deliveries, view activity reports, and register new packages.

## Features:
- **Admin Login**: Admins can log in to manage package deliveries, view reports, and register new packages.
- **User Login**: Users can log in to track their packages and view their activity reports.
- **Package Management**: Admins can pick up, delete, or manage the delivery status of packages.
- **Reporting**: Admins and users can view detailed reports on package activity.
- **Package Registration**: Admins can register new packages, assigning a unique package ID, student ID, description, and status.

## Requirements:
This system relies on the following text-based databases to store information:

1. **`packages.txt`**: A file containing information about registered packages.
2. **`admin_reports.txt`**: A file where admin activity reports are saved (e.g., package pickup, deletion).
3. **`reports.txt`**: A user-specific report file where package activities for each user are logged.
4. **`users.txt`**: A file containing user credentials (college ID, password, and name) for user login authentication.

### Sample Database Files:

#### `users.txt`
The file contains user details in the following format:
```
Name, College ID, Password
John Doe, ABC123, password123
Jane Smith, XYZ456, password456
```

#### `packages.txt`
Each line in this file contains package information in the following format:
```
Package UID, Student ID, Package Description, Status (Pending/Delivered), Arrival Date
PKG001, ABC123, Textbook, Pending, 2024-12-25 10:00:00
PKG002, XYZ456, Laptop, Pending, 2024-12-24 14:00:00
```

#### `admin_reports.txt`
This file stores admin actions and timestamps, such as picking up or deleting packages. Example:
```
PKG001, ABC123, Admin01, 2024-12-26 11:00:00
PKG002, XYZ456, Admin02, 2024-12-26 11:15:00
```

#### `reports.txt` (for each user)
Each user's report is saved in a separate file with a prefix `reports.txt` followed by their name or college ID. Example for a report file:
```
PKG001, ABC123, Admin01, 2024-12-26 11:00:00
```

## How to Run the Program:
1. **Download and install Python** (if not already installed):  
   Download Python from [here](https://www.python.org/downloads/).

2. **Prepare the database files**:
   - Create the required text files (`users.txt`, `packages.txt`, `admin_reports.txt`) in the same directory where this script is located.
   - Ensure these files have data in the correct format as described above.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the Python script is located.
   - Run the following command:
     ```bash
     python package_management_system.py
     ```

4. **Interact with the system**:
   - The program will prompt for admin or user login credentials.
   - Admins can manage packages, view reports, and register new packages.
   - Users can track their orders and view personal activity reports.

## Required Libraries:
The program only uses built-in Python libraries, so no additional packages need to be installed.

- **os**: For interacting with the operating system.
- **datetime**: For generating timestamps for package activities.

## Troubleshooting:
- **File Not Found Error**: Ensure that the database files (`users.txt`, `packages.txt`, etc.) are present in the same directory as the Python script.
- **Permission Errors**: Make sure you have write permissions to modify the database files on your system.

## Future Enhancements:
- Add more robust error handling (e.g., file not found, permission errors).
- Support for a more complex database system (e.g., SQLite or MySQL).
- Implement email notifications or SMS alerts for package status updates.

## License:
This project is open-source and available for use under the MIT License.
