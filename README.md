# CSIT-355-Database-Systems---Final-Project
Design a database system for the university, which contains the information of students (identified by student ID) and courses (identified by course ID). Students also a have student names. Courses have a course name and the number of credits. Students enroll courses.

Task 1: Database Design
Create a design.pdf file which includes the following information:

1. Provide your relational schema definitions in text form, including the attributes for each
relation and the types of all the attributes. Make sure to clearly indicate your chosen
keys (including primary and foreign). You are allowed flexibility on the exact attribute
types you use for your schema, as long as they reasonably match the specification above
(e.g., in terms of number types, string types).

2. Provide an Entity-Relation (ER) diagram that describes your schemas.

Task 2: Database Application

1. Create a database including all the relations designed in Task 1. Insert the information of
at least 5 students, 5 courses, and 10 enrollments.

2. The application must have a command-line interface menu that allows the user to select
one option as below. Once that menu function is completed, the program must return
to the main menu. For each menu option, you are allowed (and even recommended, if
needed) to have multiple steps to complete the tasks.
Student Menu:

Application starts by requesting student’s ID. If (-1) is introduced, a new student is created, and
the user is prompted for all necessary information. 

<img width="800" height="522" alt="Screenshot 2026-02-13 141919" src="https://github.com/user-attachments/assets/0390fdcf-8e93-4215-9280-0fdb51e67e5f" />


The main menu is the following:

L – List: lists all records in the course table

<img width="300" height="200" alt="Screenshot 2026-02-13 141949" src="https://github.com/user-attachments/assets/fa4dc80f-5168-40e4-b859-68428f9d2404" />


E – Enroll: enrolls the active student in a course; user is prompted for course ID; check for
conflicts, i.e., student cannot enroll twice in same course

<img width="300" height="200" alt="Screenshot 2026-02-13 142112" src="https://github.com/user-attachments/assets/4e8aa2f7-f743-4206-8dbf-ac506129cdb3" />


W – Withdraw: deletes an entry in the Enrolled table corresponding to active student; student
is prompted for course ID to be withdrawn from

<img width="300" height="200" alt="Screenshot 2026-02-13 142239" src="https://github.com/user-attachments/assets/cf70e44d-2e1f-4f14-b7aa-e2fa59192552" />


S – Search: search course based on substring of course name which is given by user; list all
matching courses

<img width="300" height="200" alt="Screenshot 2026-02-13 142321" src="https://github.com/user-attachments/assets/e79250be-8e10-41f1-a3b7-c8b8b6c6e7ae" />


M – My Classes: lists all classes enrolled in by the active student.

<img width="300" height="200" alt="Screenshot 2026-02-13 142418" src="https://github.com/user-attachments/assets/b6776969-4468-41d5-8a8c-00391a312592" />


X – Exit: exit application

<img width="300" height="200" alt="Screenshot 2026-02-13 142502" src="https://github.com/user-attachments/assets/94fc89c7-6fe7-4984-9d1c-ff1a9e16e3b3" />

