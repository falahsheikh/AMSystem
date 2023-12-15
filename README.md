# Student Record System (SRS) using Tkinter and MySQL

## Introduction

This is a simple Student Record System (SRS) implemented using Tkinter for the graphical user interface and MySQL for database management. The system allows users to add, update, delete, and view student records.

## Prerequisites

Before running the application, ensure that you have the required Python libraries installed:

- Tkinter
- pymysql

You can install them using the following commands:

```bash
pip install tk
pip install pymysql
```

## Getting Started

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-repo.git
```

2. Navigate to the project directory:

```bash
cd your-repo
```

## Running the Application

To run the Student Record System, execute the following command in your terminal or command prompt:

```bash
python your_file_name.py
```

## Features

- Add new student records.
- Update existing student records.
- Delete selected student records.
- View all student records in a tabular format.

## Usage

1. Launch the application.
2. Enter the student details in the "Enter Details" section.
3. Click the "Save" button to add a new record.
4. To update a record, select the record from the table, modify the details, and click the "Update" button.
5. To delete a record, select the record from the table and click the "Delete" button.
6. The "Clear" button resets the entry fields.
7. The table displays all student records with columns such as Student UID, Full Legal Name, Faculty, etc.

## Database Configuration

The application is configured to use a MySQL database. Ensure that you have a MySQL server running locally with a database named 'srs1'. You can adjust the database configuration in the code if needed.

```python
conn = pymysql.connect(host='localhost', user='root', password='', database='srs1')
```

## Important Note

- This system assumes a local MySQL database without authentication (password='') for simplicity.
- Modify the code to include proper database credentials and security measures in a production environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
