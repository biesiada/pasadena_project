#!/usr/bin/env python
# coding: utf-8

# 
# # Method 1: Download database from Google drive after permission granted
# 
# (!) executes in system enviorment
# 
# In Google Colab, the exclamation point (!) is used to indicate that the following command should be executed in the command-line interface (CLI) of the underlying operating system, rather than within the Python interpreter or notebook environment

# In[1]:


#! gdown -- <replace this with google drive link id only>


# # Method 2: Mount Google Drive
# Must copy authentication code from drive

# In[ ]:


# uncomment the two lines below to mount entire Google drive
# from google.colab import drive
# drive.mount('/content/drive')


# # Method 3: Upload database from directory

# In[2]:


from google.colab import files
uploaded = files.upload() # prompt to select a file to upload


# # View the tables in SQLite
#  This code will retrieve the names of all tables in the db file and print them to the console. 
# Note that the file name and path should match the location of your database file in Google Colab.
# 
# 

# In[3]:


import sqlite3
conn = sqlite3.connect('student_data.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(tables)


# # View the row data in each table
# 
# This code first creates a connection to the student_data.db file, then retrieves all rows from each of the three tables using a SELECT statement. The fetchall() method is used to retrieve the result of each query, which is a list of tuples representing the rows in the table.
# 
# Finally, the code prints out each row of each table using a for loop, so you can see the contents of each table.

# In[4]:


# view the row data within each table
import sqlite3
conn = sqlite3.connect('student_data.db')
cursor = conn.cursor()

# Retrieve rows from tblStudents
cursor.execute("SELECT * FROM tblStudents")
students = cursor.fetchall()
print("Rows from tblStudents:")
for row in students:
    print(row)

# Retrieve rows from tblFeedback
cursor.execute("SELECT * FROM tblFeedback")
feedbacks = cursor.fetchall()
print("Rows from tblFeedback:")
for row in feedbacks:
    print(row)

# Retrieve rows from tblScores
cursor.execute("SELECT * FROM tblScores")
scores = cursor.fetchall()
print("Rows from tblScores:")
for row in scores:
    print(row)


# # Run a where clause on Joe from the student table
# 
# This code connects to a SQLite database called student_data.db, executes a SELECT statement with a WHERE clause to select all rows from the tblStudents table where the fname column is equal to joe, fetches the results, prints the results to the console, and closes the connection.
# 
# In more detail, the code first imports the sqlite3 module. Then, it connects to the database using the connect() method. Next, it creates a cursor using the cursor() method. Then, it executes the SELECT statement using the execute() method. Next, it fetches the results using the fetchall() method. Then, it prints the results to the console using a for loop. Finally, it closes the connection using the close() method.
# 

# In[5]:


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

