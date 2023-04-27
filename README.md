<img src="./pasadena_cc_logo.png" width="200" height="150">

# 1. Example 1-validation

This file demonstrates how to validate phone numbers in Python.

### Importing modules

The code first imports the os and re modules. The os module provides a way to interact with the operating system, directories, and functions. The re module provides support for regular expressions in Python.

```python
import os
import re
```

### Defining a function

The code then defines a function called print_phone_number(). This function takes a filename as its argument and checks the file for a valid phone number. A valid phone number is in the format XXX-XXX-XXXX, where X is a digit between 0 and 9.

```python
def print_phone_number(filename):
  """
  This function checks a file for a valid phone number.

  Args:
    filename: The name of the file to check.

  Returns:
    1 if the phone number is valid, 0 if the phone number is not valid, or -1 if the phone number is plagiarized.
  """

  # Open the file.
  with open(filename, "r") as f:
    # Read the file line by line.
    for line in f:
      # Check if the line contains a valid phone number.
      if re.match(r"^\d{3}-\d{3}-\d{4}$", line):
        return 1
      else:
        return 0

  return -1
```

### Main loop

The code then enters a loop. In the loop, the code prompts the user to enter a filename. If the user enters quit, the loop terminates. Otherwise, the code checks if the file exists. If the file does not exist, the code prints a message and continues to the next iteration of the loop. If the file does exist, the code calls the print_phone_number() function.

```python
# Prompt the user to enter a filename.
while True:
  filename = input("Enter a filename or quit: ")

  # Check if the user entered quit.
  if filename == "quit":
    break

  # Check if the file exists.
  if not os.path.exists(filename):
    print("The file {} does not exist.".format(filename))
    continue

  # Call the print_phone_number() function.
  score = print_phone_number(filename)

  # Print the score.
  print("The score for {} is {}".format(filename, score))
```


# 2. Example 2 - database 

This Python code creates a database of student data. The code first imports the necessary modules, including `re`, `sqlite3`, and `os`. It then connects to the database and creates three tables: `tblStudents`, `tblFeedback`, and `tblScores`.

### Modules

```markdown

import re
import sqlite3
import os

```
### Prompts user for data

The code then prompts the user for a last name to search for in the directory. It then loops through the files in the directory and checks if they end with the specified last name. If they do, the code extracts the first and last name from the filename, prompts the user for feedback and a score, and inserts the student data into the database.

```markdown

lname_search = input("Enter the last name to search for in the directory: ")

for file in os.listdir():
  if file.endswith(lname_search + ".ipynb"):
    # Extract the first and last name from the filename
    fname_lname = file.split("_")[0].split(".")[0].split("-")
    fname = fname_lname[0]
    lname = fname_lname[1]

    # Prompt the user to input feedback and score for this submission
    feedback = input("Enter feedback for " + fname + " " + lname + ": ")
    score = input("Enter score for " + fname + " " + lname + ": ")

    # Insert student data into tblStudents and get the auto-generated student_id
    c.execute("INSERT INTO tblStudents (fname, lname) VALUES (?, ?)", (fname, lname))
    student_id = c.lastrowid

    # Insert feedback and score into tblFeedback and tblScores using the student_id
    c.execute("INSERT INTO tblFeedback (student_id, feedback) VALUES (?, ?)", (student_id, feedback))
    c.execute("INSERT INTO tblScores (student_id, score) VALUES (?, ?)", (student_id, score))
```
### Closes database connection


The code finally commits the changes and closes the database connection.

```python
conn.commit()
conn.close()
``````

# 3. Colab pasadena mydatabase file 

This code will connect to a SQLite database, view the tables in the database, view the row data in each table, and run a where clause on a student named "Joe" from the student table.

### Method 1: Download database from Google drive after permission granted

In Google Colab, the exclamation point (!) is used to indicate that the following command should be executed in the command-line interface (CLI) of the underlying operating system, rather than within the Python interpreter or notebook environment.

```python
#! gdown -- <replace this with google drive link id only>
```

### Method 2: Mount Google Drive

Must copy authentication code from drive

```python
# uncomment the two lines below to mount entire Google drive
# from google.colab import drive
# drive.mount('/content/drive')
```

### Method 3: Upload database from directory

```python
from google.colab import files
uploaded = files.upload() # prompt to select a file to upload
```

### View the tables in SQLite

This code will retrieve the names of all tables in the db file and print them to the console.

```python
import sqlite3
conn = sqlite3.connect('student_data.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(tables)
```

### View the row data in each table

This code first creates a connection to the student_data.db file, then retrieves all rows from each of the three tables using a SELECT statement. The fetchall() method is used to retrieve the result of each query, which is a list of tuples representing the rows in the table. Finally, the code prints out each row of each table using a for loop, so you can see the contents of each table.

```markdown
### view the row data within each table
import sqlite3
conn = sqlite3.connect('student_data.db')
cursor = conn.cursor()

### Retrieve rows from tblStudents
cursor.execute("SELECT * FROM tblStudents")
students = cursor.fetchall()
print("Rows from tblStudents:")
for row in students:
    print(row)

### Retrieve rows from tblFeedback
cursor.execute("SELECT * FROM tblFeedback")
feedbacks = cursor.fetchall()
print("Rows from tblFeedback:")
for row in feedbacks:
    print(row)

### Retrieve rows from tblScores
cursor.execute("SELECT * FROM tblScores")
scores = cursor.fetchall()
print("Rows from tblScores:")
for row in scores:
    print(row)
```

### Run a where clause on Joe from the student table

This code connects to a SQLite database called student_data.db, executes a SELECT statement with a WHERE clause to select all rows from the tblStudents table where the fname column is equal to joe, fetches the results, prints the results to the console, and closes the connection.

In more detail, the code first imports the sqlite3 module. Then, it connects to the database using the connect() method. Next, it creates a cursor using the cursor() method. Then, it executes the SELECT statement using the execute() method. Next, it fetches the results using the fetchall() method. Next, it prints the results to the console using a for loop. Finally, it closes the connection using the close() method.

### Summary
The code first connects to the database called student_data.db. Then, it creates a cursor object. Next, it executes a SELECT statement with a WHERE clause to select all rows from the tblStudents table where the fname column is equal to joe. Finally, it prints the results to the console and closes the connection.

```markdown
import sqlite3

# Connect to the database
connection = sqlite3.connect('student_data.db')

# Create a cursor
cursor = connection.cursor()

# Execute a SELECT statement with a WHERE clause
cursor.execute('SELECT * FROM tblStudents WHERE fname = "joe"')

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
connection.close()
```







