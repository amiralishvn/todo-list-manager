# Python To-Do List Manager

A command-line To-Do List application built with Python, using Object-Oriented Programming (OOP) and CSV file handling to manage tasks and persist data between program sessions.

## Features

* **Add Tasks:** Create tasks with a unique ID, name, description, and priority.
* **Remove Tasks:** Delete tasks using their IDs.
* **View Tasks:** Display all saved tasks and their details.
* **Priority Management:** Assign priorities to tasks (High, Medium, or Low).
* **CSV Storage:** Save tasks to a CSV file.
* **Automatic Data Persistence:** Load existing tasks when the application starts and save changes automatically.
* **Interactive CLI:** Manage tasks through a simple text-based menu.

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* CSV file handling
* Python standard library

## Getting Started

### Prerequisites

Python 3.8 or later.

No third-party packages are required.

### Installation

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd YOUR_REPOSITORY_NAME
   ```

3. Run the application:

   ```bash
   python main.py
   ```

The application creates and updates `tasks.csv` to store task data.

## Usage

After launching the application, use the interactive menu to:

1. Add a new task.
2. Remove an existing task.
3. View all tasks.
4. Save tasks to CSV.
5. Exit the application.

Tasks are saved locally so they can be loaded in subsequent sessions.

## Project Structure

```text
todo-list-manager/
├── main.py
├── tasks.csv          # Generated at runtime
├── requirements.txt
├── .gitignore
└── README.md
```

## Learning Objectives

This project demonstrates practical implementation of:

* Classes, objects, and constructors
* Instance attributes and methods
* Managing collections of objects
* CRUD operations (Create, Read, and Delete)
* Reading and writing CSV files
* Interactive menus and control flow
* Basic data persistence

## Future Improvements

* Validate task priorities and unique IDs.
* Prevent duplicate task IDs.
* Handle missing or corrupted CSV files.
* Add task completion status.
* Support task editing and filtering by priority.
* Add automated unit tests.

## License

This project is available for educational and portfolio purposes. A license can be added if the project is intended for public reuse.
