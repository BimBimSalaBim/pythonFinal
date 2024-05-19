
# Student Management System

## Overview

This project is a Student Management System designed to manage student information, calculate grades, and generate reports for a class. The system allows you to add, remove, edit student details, and sort students by their last name. It provides functionalities to save reports to files and view individual student information. 

## Features

- Add new students to the system.
- Remove existing students.
- Edit scores of students.
- View individual student information.
- Print a detailed report of all students.
- Print a summarized list of students.
- Save reports to files.
- Sort students by their last names.

## Class Descriptions

### `Student`
The `Student` class holds all the information for a student including:
- `firstName`: The first name of the student.
- `lastName`: The last name of the student.
- `fullName`: The full name of the student.
- `id`: The student ID.
- `scores`: List of test scores.
- `quiz`: Quiz score.

#### Methods:
- `__init__(self, firstName, lastName)`: Initializes a new student with a first and last name.
- `add_quiz(self, quiz)`: Adds a quiz score.
- `add_score(self, score)`: Adds a test score.
- `getLowest(self, scores)`: Returns the lowest score.
- `get_grade(self)`: Calculates and returns the average grade.
- `get_LetterGrade(self)`: Returns the letter grade based on the average grade.

### Utility Functions
- `reportPrint(students, className, classRoom)`: Prints a detailed report for all students.
- `printList(students)`: Prints a summarized list of students.
- `SortList(students)`: Sorts the list of students by their last names.
- `saveReport(students, className, classRoom)`: Saves the report to a file.
- `partialSearch(student, name)`: Searches for a student by partial name match.
- `editScores(students, name)`: Edits the scores of a specified student.
- `inList(name, students)`: Checks if a student is in the list.
- `printStudent(students)`: Prints information for a specified student.
- `addStudent(students)`: Adds a new student to the list.
- `removeStudent(students)`: Removes a student from the list.
- `writeFile(students)`: Writes the student data to a file.
- `fileImport()`: Imports student data from a file.
- `menu()`: Displays the main menu.

## Getting Started

### Prerequisites
- Python 3.x

### Running the Program

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Run the program:
   ```sh
   python student_management_system.py
   ```

### Main Menu Options
1. **Print Report**: Prints a detailed report of all students.
2. **Print Student List**: Prints a summarized list of all students.
3. **View Student**: View detailed information for a specific student.
4. **Save Report to File**: Saves the report to a file.
5. **Edit Scores**: Edits the scores for a specific student.
6. **Add Student**: Adds a new student to the list.
7. **Sort Students**: Sorts the students by their last name.
8. **Remove Student**: Removes a student from the list.
9. **Quit**: Exits the program.

## Example Input File Format
```
Introduction to Computer Programming Fundamentals CSCI 1
MBA 315
John Adams
111223333 99 87 93 90 90 89 91
Margarete Aiko
777777777 100 80 100 100 100 100 100
Nancy Brown Tyler
997766555 100 80 70 50 60 90 100
Jose Cruze
888778878 99 80 70 90 80 90 100
Philip Grdener
777880066 90 80 70 80 60 90 100
Phil Jordan
777886666 100 80 70 50 -60 90 100
Willy Smith Jr.
222114444 0 90 73 67 77 70 80
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Thanks to Johannes Charra for providing the sorting expression on StackOverflow.

For any questions or support, please contact [your-email@example.com].
