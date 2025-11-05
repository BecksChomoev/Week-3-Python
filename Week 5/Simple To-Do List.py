print("Welcome to Simple To-Do List")
tasks = []
options

while True:
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Quit")
    print("Please choose what you would like to do. Make sure to choose the number of the function.")
    user_input = int(input("Enter your choice: "))

    if user_input == 1:
        print("Task Added")
    elif user_input == 4:
        break