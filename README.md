# python-dev-intern-task-2-to-do-list-app
Python Developer Internship Task 2 (To Do List Application - Console Based) 

## Types of error while handling file: ##
1. FileNotFoundError - file does not exist
2. PermissionError - do not have permission to access the file
3. IsADirectoryError - trying to open directory as file
4. UnicodeDecodeError - while decoding the file with incompatible encoding
   - with open("encoded_file.txt", "r", encoding="latin-1") as f:
5. IOError - due to failure in any input/output operations, and it does not fall in any of the above category. OSError is the base class for IOError

## How the code works ##

when we execute the command python todo.py in terminal, we get
1. Name of App with the menu of actions we would like to do.
   - 1. Add New Task
   - 2. Remove Task
   - 3. View Tasks
   - 4. Exit
2. Invalid selection will display the error message with menu but this time without app name.
3. Depending upon user selection, if user selects to add new task
   - User can enter a new task
   - Duplicate check is performed
   - If found to be duplicate, user is given a chance to again add something else
   - If there is no duplicate, it gets added to file which is opened in append mode
4. If user selects to view items
   - The file is opened in read mode.
   - If file does not exist, the message is displayed accordingly
   - If file is empty, then user is given chance to add something.
   - In case of any data, it reads the data and display it with the task number.
   - This function can be used in 2 ways
     - If read mode is 1, it means it will just display the data with any return type.
     - If read mode is other than 1, it means further actions will be performed after the list view, and it will return list type of data.
5. If user select to remove any item
   - First the tasks are listed.
   - User is asked to mention the task number.
   - Invalid input will not do anything.
   - Valid input will delete the task and update the file by opening it in write mode and will display the message accordingly.

## Extras (Not included in task) ##

1. To edit a task, we can remove it and add it again in list via console. If sequence matters, then another way is to mention updated task at any index and update as it is done in remove item via list data type.
2. For sorting, use another list to perform the sorting and get the updated list.