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
the user is prompted for all necessary information. The main menu is the following:

L – List: lists all records in the course table

E – Enroll: enrolls the active student in a course; user is prompted for course ID; check for
conflicts, i.e., student cannot enroll twice in same course

W – Withdraw: deletes an entry in the Enrolled table corresponding to active student; student
is prompted for course ID to be withdrawn from

S – Search: search course based on substring of course name which is given by user; list all
matching courses

M – My Classes: lists all classes enrolled in by the active student.

X – Exit: exit application
