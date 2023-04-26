# Pasadena project

### Example 1-validation 

1.	Modules imported
a.	The code first imports the os and re modules. The os module provides a way to interact with the operating system, directories, and functions. The re module provides support for regular expressions in Python.
2.	Print Phone number function 
a.	The code then defines a function called print_phone_number(). This function takes a filename as its argument and checks the file for a valid phone number. A valid phone number is in the format XXX-XXX-XXXX, where X is a digit between 0 and 9.
b.	The code then defines two variables: phone_numbers and scores. The phone_numbers variable is a dictionary that stores the phone numbers found in the files. The scores variable is a dictionary that stores the scores for each file.
3.	Last part – loop 
a.	The code then enters a loop. In the loop, the code prompts the user to enter a filename. If the user enters quit, the loop terminates. Otherwise, the code checks if the file exists. If the file does not exist, the code prints a message and continues to the next iteration of the loop. If the file does exist, the code calls the print_phone_number() function. The print_phone_number() function returns a value of 1 if the phone number is valid, 0 if the phone number is not valid, or -1 if the phone number is plagiarized. The code then stores the value returned by print_phone_number() in the scores dictionary.
b.	After the loop terminates, the code prints the scores for each file.


### Example 1 – database 

1.	Importing modules
o	The re module provides support for regular expressions in Python.
o	The sqlite3 module provides a Python interface to the SQLite database.
o	The os module provides a way to interact with the operating system, directories, and files.
o	The script first imports the re, sqlite3, and os modules. 
2.	Database creation 
o	It then connects to the database student_data.db. If the database does not already exist, the script creates it.
o	The script then prompts the user for the last name to search for in the directory. 
o	It then loops through the files in the directory. For each file, the script checks if the file ends with the last name that the user specified. If the file ends with the last name, the script extracts the first and last name from the filename.
3.	Prompts user
o	The script then prompts the user to input feedback and score for the submission. It then inserts the student data into the tblStudents table and gets the auto-generated student_id. The script then inserts the feedback and score into the tblFeedback and tblScores tables using the student_id.
4.	Database closes
o	Finally, the script commits the changes to the database and closes the database connection.

### Colab pasdena mydatabase



