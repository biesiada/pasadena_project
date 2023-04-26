# Project explanation for processing student files: ![My_image](./pasadena_cc_logo.png)

# Example 1-validation

This example demonstrates how to validate phone numbers in Python.

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
