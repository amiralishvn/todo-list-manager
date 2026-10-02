import csv
import os


class Task:
    def __init__(self, workCode, workName, workDescription, workPriority):
        self.code = workCode
        self.name = workName
        self.description = workDescription
        self.priority = workPriority

class ToDoList:
    def __init__(self):
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)

    def removeTask(self,taskCode):
        for task in self.tasks:
            if task.code == taskCode:
                self.tasks.remove(task)
                print("Task Removed Permanently!")
                return
        print("Task not found!")

    def showTasks(self):
        for task in self.tasks:
            print("Task ID: ", task.code)
            print("Task Name: ", task.name)
            print("Task Description: ", task.description)
            print("Task Priority: ", task.priority)
            print("--------------------------------------------")

    def saveTasks(self):
        with open("tasks.csv", "w", newline = "", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Code", "Name", "Description", "Priority"])

            for task in self.tasks:
                writer.writerow([task.code, task.name, task.description, task.priority])

        print("Tasks Saved!")

    def loadTasks(self):
        with open("tasks.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                task = Task(row["Code"], row["Name"], row["Description"], row["Priority"])
                self.tasks.append(task)

        print("Tasks Loaded!")



myList = ToDoList()

if os.path.exists("tasks.csv"):
    myList.loadTasks()

while True:
    print("\n========== TO-DO APP ==========")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Save Tasks")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("====================================================================")
        code = input("Enter Task ID: ")
        name = input("Enter Task Name: ")
        description = input("Enter Task Description: ")
        priority = input("Enter Priority [H/M/L]: ").upper()

        task = Task(code, name, description, priority)
        myList.addTask(task)
        myList.saveTasks()

    elif choice == "2":
        print("====================================================================")
        code = input("Enter Task ID to remove: ")
        myList.removeTask(code)
        myList.saveTasks()

    elif choice == "3":
        print("====================================================================")
        myList.showTasks()

    elif choice == "4":
        print("====================================================================")
        myList.saveTasks()

    elif choice == "5":
        print("====================================================================")
        myList.saveTasks()
        print("Goodbye!")
        break

    else:
        print("====================================================================")
        print("Invalid option! Please try again.")