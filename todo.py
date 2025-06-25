TASK_FILE_NAME = "tasks.txt"

def display_menu(fresh_start:int):
    if fresh_start == 1:
        print("To Do List Application:")
    print("Menu")
    print("1. Add New Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    try:
        action = int(input("Please select an option (1-4):"))

        if action == 1:
            add_task()
        elif action == 2:
            remove_task()
        elif action == 3:
            view_tasks(1)
        elif action == 4:
            exit()
        else:
            print("Invalid selection.")
            display_menu(0)
    except ValueError:
        print("Invalid selection.")
        display_menu(0)

def is_duplicate_entry(task: str) -> bool:
    try:
        with open(TASK_FILE_NAME, "r") as task_file:
            # returns list
            tasks = task_file.read().splitlines()
            if task in tasks:
                return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def add_task():
    print("You selected: Add New Task")
    task = input("Please enter an task: ").capitalize()
    if is_duplicate_entry(task):
        print("The task already exists. Try adding something else...")
        add_task()
    else:
        with open(TASK_FILE_NAME, "at") as task_file:
            task_file.write(task + "\n")

def remove_task():
    print("You selected: Remove Task")
    # send any value other than 1, 1 means reading, other than 1 means reading for remove action
    tasks_data = view_tasks(0)
    no_error = tasks_data[0]
    task_count = tasks_data[1]
    tasks = tasks_data[2]

    if no_error:
        try:
            task_no = int(input("Please enter an task number to remove: "))
            if task_no > task_count or task_no <= 0:
                print("Invalid task number.")
            else:
                removed_task = tasks[task_no - 1]
                tasks.pop(task_no-1)
                with open(TASK_FILE_NAME, "wt") as task_file:
                    for task in tasks:
                        task_file.write(task + "\n")
                    else:
                        print(f"Task '{removed_task}' has been removed.")
        except ValueError:
            print("Invalid selection.")

def view_tasks(read_mode:int) -> list | None:
    if read_mode == 1:
        print("You selected: View Tasks")
    try:
        with open(TASK_FILE_NAME, "r") as task_file:
            # returns list
            tasks = task_file.read().splitlines()
            task_count = len(tasks)
            if task_count == 0:
                if read_mode == 1:
                    print("No tasks found in TO DO list.")
                else:
                    print("TO DO List is empty.")
                    return [False, 0, []]
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                    if read_mode != 1:
                        if index == task_count:
                            return [True, task_count, tasks]
    except FileNotFoundError:
        if read_mode == 1:
            print("TO DO List does not exists. Try adding the first task. Press enter to continue:")
            add_task()
        else:
            print("TO DO List does not exists. ")
            return [False, 0, []]
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [False, 0, []]

def main():
    display_menu(1)

if __name__ == "__main__":
    main()