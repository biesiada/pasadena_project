<img src="./pasadena_cc_logo.png" width="200" height="150">

# Example 1-validation

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


# Example 2 - database 

This Python code creates a database of student data. The code first imports the necessary modules, including `re`, `sqlite3`, and `os`. It then connects to the database and creates three tables: `tblStudents`, `tblFeedback`, and `tblScores`.

```markdown

import re
import sqlite3
import os

```

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

The code finally commits the changes and closes the database connection.

```python
conn.commit()
conn.close()
``````









