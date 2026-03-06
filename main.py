from modules.calculator import calculator_menu
from modules.notes_manager import add_note, view_notes
from modules.timer_tool import start_timer
from modules.file_organizer import organize_files
from modules.unit_converter import unit_converter
from modules.backup_restore import backup_data, restore_data


def main():
    while True:
        print("\n===== PERSONAL PRODUCTIVITY SUITE =====")
        print("1. Calculator")
        print("2. Add Note")
        print("3. View Notes")
        print("4. Timer")
        print("5. File Organizer")
        print("6. Unit Converter")
        print("7. Backup Data")
        print("8. Restore Data")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator_menu()

        elif choice == "2":
            add_note()

        elif choice == "3":
            view_notes()

        elif choice == "4":
            start_timer()

        elif choice == "5":
            organize_files()

        elif choice == "6":
            unit_converter()

        elif choice == "7":
            backup_data()

        elif choice == "8":
            restore_data()

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()