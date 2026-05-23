
# Student Information Validator
A simple Python program that validates student information based on predefined rules and displays the current date and time after validation.

![image](https://github.com/owenlim225/Student-identification/assets/87555304/feab3f21-67d5-4152-a12b-5257cad80737)

## Features

- Validates a student's:
  - ID number
  - Name
  - Course
- Checks if:
  - The student ID contains exactly **9 digits**
  - The student name contains only alphabetic characters and spaces
- Displays:
  - Validation result
  - Current date and time

---

## Requirements

- Python 3.x

No external libraries are required.

---

## How It Works

The program accepts input in the following format:

```text
StudentID - Name - Course

Example:

123456789 - John Doe - Computer Science

The program then validates the input using these rules:

Field	Validation Rule
ID Number	Must contain exactly 9 digits
Name	Must only contain letters and spaces
Course	Accepted as plain text
Example Usage
Valid Input
Testing Student: 123456789 - John Doe - Computer Science

Output:

Student information is valid.
2026-05-23 13:45:00.123456
Invalid Input (Short ID)
Testing Student: 12345 - Jane Doe - Mathematics

Output:

Student information is not valid.
2026-05-23 13:45:10.654321
Invalid Input (Name Contains Numbers)
Testing Student: 987654321 - Alice123 - Physics

Output:

Student information is not valid.
2026-05-23 13:45:20.111111
Invalid Input (Special Characters in Name)
Testing Student: 123456789 - Bob! - Engineering

Output:

Student information is not valid.
2026-05-23 13:45:30.222222
File Structure
.
├── main.py
└── README.md
Code Overview
Student Class

The Student class stores student information and contains validation logic.

Methods
Method	Description
__init__()	Initializes student data
__str__()	Returns formatted student information
validate_info()	Validates the student data
Validation Rules Summary
✅ Name must contain only letters and spaces
✅ Student ID must be exactly 9 digits
❌ Numbers or special characters in names are invalid
❌ IDs shorter or longer than 9 digits are invalid
Run the Program

Use the following command in the terminal:

python main.py
