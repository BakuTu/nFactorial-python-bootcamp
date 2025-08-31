# Date 2025-08-27

# Task manager - Simple Vision

# Import required modules
from datetime import datetime, timedelta    # Import datetime and timedelta for working with time

# Storage for tasks
task_list = []  # Create an empty list for storing tasks
display_completed_task = False # Flag for showing completed tasks
# Create new task
date_time = datetime.now()  # Get the current time when task is created
time_to_create_task  = date_time.strftime("%Y-%m-%d %H:%M")  # Format created time
deadline_number_days = int(input("Days until deadline: "))  # Ask the user how many days until deadline
data = date_time + timedelta(days=deadline_number_days) # Calculate deadline by adding days
deadline_variable = data.strftime("%Y-%m-%d %H:%M") # Format deadline time

# Fill dictionary with task data
task = {
    "name": input("New task name: "),   # Task name
    "created_time": time_to_create_task,    # Created time
    "status": input("New task status: "),   # Task status
    "deadline": deadline_variable,  # Deadline
}

# Add task to the list
task_list.append(task)  # Add the task to the list

print("\nTask added successfully:") # Show added task
print("Name:", task["name"])
print("Created_time:", task["created_time"])
print("Status:", task["status"])
print("Deadline:", task["deadline"])
