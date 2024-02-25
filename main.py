class Task:
    def __init__(self, title, content, deadline, status="To do"):
        """
        Initializes a task object with title, content, deadline, and status.

        Parameters:
            title (str): The title of the task.
            content (str): The content or description of the task.
            deadline (str): The deadline of the task in the format YYYY-MM-DD.
            status (str): The status of the task, defaults to "To do".
        """
        self.title = title
        self.content = content
        self.deadline = deadline
        self.status = status

    def __str__(self):
        """
        Returns a string representation of the task.
        """
        return f"Title: {self.title}\nContent: {self.content}\nDeadline: {self.deadline}\nStatus: {self.status}"


class TaskManager:
    def __init__(self):
        """
        Initializes a TaskManager object with an empty list of tasks.
        """
        self.tasks = []

    def add_task(self, task):
        """
        Adds a task to the task manager.
        """
        self.tasks.append(task)

    def remove_task(self, title):
        """
        Removes a task from the task manager based on its title.
        """
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' deleted.")
                return
        print(f"Can't find '{title}' task.")

    def display_tasks(self):
        """
        Displays all tasks currently in the task manager.
        """
        if self.tasks:
            for index, task in enumerate(self.tasks, start=1):
                print(f"Task {index}:\n{task}\n")
        else:
            print("No saved task.")

    def update_task_status(self, title, new_status):
        """
        Updates the status of a task.
        """
        for task in self.tasks:
            if task.title == title:
                task.status = new_status
                print(f"Task '{title}' status updated: {new_status}.")
                return
        print(f"Can't find '{title}' task.")

    def update_task_deadline(self, title, new_deadline):
        """
        Updates the deadline of a task.
        """
        for task in self.tasks:
            if task.title == title:
                task.deadline = new_deadline
                print(f"Task '{title}' deadline updated: {new_deadline}.")
                return
        print(f"Can't find '{title}' task.")


def display_menu():
    """
    Displays the menu options for the task management application.
    """
    print("\n===== Menu =====")
    print("1. Display tasks")
    print("2. Add task")
    print("3. Modify task status")
    print("4. Modify task deadline")
    print("5. Delete task")
    print("6. Exit")


def main():
    """
    Main function to run the task management application.
    """
    task_manager = TaskManager()

    while True:
        display_menu()
        choice = input("Please choose an option: ")

        if choice == "1":
            task_manager.display_tasks()
        elif choice == "2":
            title = input("Add task title: ")
            content = input("Add task content: ")
            deadline = input("Add deadline (format YYYY-MM-DD): ")
            new_task = Task(title, content, deadline)
            task_manager.add_task(new_task)
            print("Task added with success.")
        elif choice == "3":
            title = input("Enter the title of the task to be modified: ")
            new_status = input("Enter the new status of the task (to do or done): ")
            task_manager.update_task_status(title, new_status)
        elif choice == "4":
            title = input("Enter the title of the task to be modified: ")
            new_deadline = input("Fill the new deadline for this task (format YYYY-MM-DD): ")
            task_manager.update_task_deadline(title, new_deadline)
        elif choice == "5":
            title = input("Enter the title of the task to be deleted: ")
            task_manager.remove_task(title)
        elif choice == "6":
            print("Thank you for using our task management application. See you soon!")
            break
        else:
            print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    main()
