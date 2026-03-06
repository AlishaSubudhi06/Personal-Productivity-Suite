import json

file_path = "data/notes.json"


def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")

    note = {"title": title, "content": content}

    try:
        with open(file_path, "r") as f:
            notes = json.load(f)
    except:
        notes = []

    notes.append(note)

    with open(file_path, "w") as f:
        json.dump(notes, f, indent=4)

    print("Note added successfully")


def view_notes():
    try:
        with open(file_path, "r") as f:
            notes = json.load(f)

        for i, note in enumerate(notes, 1):
            print(f"{i}. {note['title']} - {note['content']}")

    except:
        print("No notes found")