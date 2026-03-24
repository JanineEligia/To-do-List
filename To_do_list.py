# to-do list

tasks = []

def to_do_list(tasks):
    print("What do you plan to do today?")
    print("\n 1. Add a task" 
          "\n 2. Edit a task" 
          "\n 3. Delete a task" 
          "\n 4. Exit")

    try:
        choice = int(input("Enter your choice: "))
        return choice

    except ValueError:
        print("Invalid input. Please enter a number from the choices")
        return None

while True:

    choice = to_do_list(tasks)

    if choice == 1:
        activity = input("Enter the task you want to add: ")
        tasks.append(activity)
        more= input("Add another task? ").lower()

        if more== "yes":
            continue
        
        elif more== "no":
            print(f"Here is your to-do list: \n {tasks}")

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    elif choice == 2:
        
        print(f"\nHere is your current to-do list: \n {tasks}")
        change_task = input("Enter the task you want to edit: ")

        if change_task in tasks:
            
            new_task = input("Enter the new task: ")
            index = tasks.index(change_task)
            tasks[index] = new_task
            print(f"Task '{change_task}' has been updated to '{new_task}'.")

            more= input("Add another task? ").lower()

            if more== "yes":
                continue
            
            elif more== "no":
                print(f"Here is your to-do list: \n {tasks}")

            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        
        else:
            print(f"Task '{change_task}' not found in the to-do list.")

    elif choice == 3:
         

        print(f"\nHere is your current to-do list: \n {tasks}")
        delete_task = input("Enter the task you want to delete: ")

        if delete_task in tasks:

            tasks.remove(delete_task)

            print(f"Task '{delete_task}' has been deleted.")
            more= input("Add another task? ").lower()

            if more== "yes":
                continue
            
            elif more== "no":
                print(f"Here is your to-do list: \n {tasks}")

            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


        else:
            print(f"Task '{delete_task}' not found in the to-do list.")

    elif choice == 4:

        print("Exiting the to-do list. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from the choices.")

    