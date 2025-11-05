print("Welcome to Simple To-Do List")
tasks = []
def show_options():
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Quit")
    print("Please choose what you would like to do. Make sure to choose the number of the function.")

def show_tasks(todo_list):
    for task in todo_list:
        print(task)

show_options()

while True:
    user_input = int(input("Enter your choice: "))

    if user_input == 1:
        user_add_task = input("You selected to add task to your to-do list. Enter your task: ")
        tasks.append(user_add_task)
        print("Task added to your to-do list.")
        print("What would you like to do next?.")
        show_options()
    elif user_input == 2:
        print("You chose to remove task. Which task would you like to remove?")
        show_tasks(tasks)
        user_del_task = int(input("Enter your choice: "))
        tasks.remove(user_del_task)
        print("Task removed from your to-do list.")
        print("What would you like to do next?.")
        show_options()
    elif user_input == 3:
        print("You chose to view all your to-do list.")
        show_tasks(tasks)
        print("What would you like to do next?.")
        show_options()
    else:
        break