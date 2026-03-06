import shutil

def backup_data():
    try:
        shutil.copy("data/notes.json", "data/backups/notes_backup.json")
        print("Backup created successfully")
    except:
        print("Backup failed")


def restore_data():
    try:
        shutil.copy("data/backups/notes_backup.json", "data/notes.json")
        print("Data restored successfully")
    except:
        print("Restore failed")