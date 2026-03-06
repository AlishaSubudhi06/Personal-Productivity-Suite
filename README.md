Personal Productivity Suite
📌 Project Overview

The Personal Productivity Suite is a Python-based command line application that integrates multiple productivity tools into one system.
It allows users to perform calculations, manage notes, organize files, use timers, convert units, and backup important data.

The project demonstrates object-oriented programming, modular design, file handling, and command line interfaces in Python.

🎯 Project Objectives

Build a modular Python application

Implement file handling using JSON

Create reusable modules for different tools

Provide a user-friendly menu based interface

Store and manage data across sessions

Implement backup and restore functionality

🛠 Technologies Used

Python

Git

GitHub

Visual Studio Code

📂 Project Structure
Personal-Productivity-Suite
│
├── main.py
│
├── modules
│   ├── __init__.py
│   ├── calculator.py
│   ├── notes_manager.py
│   ├── timer_tool.py
│   ├── file_organizer.py
│   ├── unit_converter.py
│   └── backup_restore.py
│
├── data
│   ├── notes.json
│   └── backups
│
└── requirements.txt
⚙️ Features
1️⃣ Calculator

Performs basic arithmetic operations:

Addition

Subtraction

Multiplication

Division

2️⃣ Notes Manager

Allows users to:

Add notes

View saved notes

Store notes using JSON

3️⃣ Timer Tool

Provides a simple countdown timer for productivity.

4️⃣ File Organizer

Automatically organizes files into folders based on file type.

5️⃣ Unit Converter

Converts different units such as:

Length

Weight

Temperature

6️⃣ Backup & Restore

Creates backup copies of data files and restores them when needed.

🚀 How to Run the Project
Step 1

Clone the repository

git clone https://github.com/AlishaSubudhi06/Personal-Productivity-Suite.git
Step 2

Open the folder in VS Code

Step 3

Run the program

python main.py
📊 Sample Menu Output
===== PERSONAL PRODUCTIVITY SUITE =====

1. Calculator
2. Notes Manager
3. Timer
4. File Organizer
5. Unit Converter
6. Backup Data
7. Restore Data
8. Exit
🧪 Testing

Each module was tested individually to ensure correct functionality.
Error handling was implemented to handle invalid inputs and file errors.

📚 Future Improvements

GUI interface using Tkinter

Cloud data storage

Advanced data analytics

Mobile integration

👩‍💻 Author

Alisha Subudhi
B.Tech Student
Trident Academy of Technology