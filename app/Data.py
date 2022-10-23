USERS = {}
CATEGORIES = {}
NOTES = []

def update_users():
    USERS.clear()
    with open('data/UsersList.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            id = line[4:40]
            category_name = line[47:len(line) - 1]
            USERS.update({f"{id}": f"{category_name}"})

def update_categories():
    CATEGORIES.clear()
    with open('data/CategoryList.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            id = line[4:40]
            category_name = line[47:len(line) - 1]
            CATEGORIES.update({f"{id}": f"{category_name}"})

def update_notes():
    NOTES.clear()
    with open('data/NotesList.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            id = line[4:40]
            user_id = line[50:86]
            category_id = line[100:136]
            date = line[143:162]
            cost = line[169:len(line)-2]
            NOTES.append([f"{id}", f"{user_id}", f"{category_id}", f"{date}", f"{cost}"])
