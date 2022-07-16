# imports PersonalAssistant.py file
from PersonalAssistant import PersonalAssistant
import json

# ADD CODE: open JSON file and pass data to PersonalAssistant class
with open("todos.json", "r") as todos, open("birthdays.json", "r") as birthdays, open("contacts.json", "r") as contacts:
    todo_list = json.load(todos)
    birthday_list = json.load(birthdays)
    contact_list = json.load(contacts)
    assistant = PersonalAssistant(todo_list, birthday_list, contact_list)

done = False

while not done:
    user_command = input("""
How can I help you?

    **** To-dos *****
    1: Get to-do list
    2: Add a to-do
    3: Remove a to-do
    4: Get Birthdays
    5: Add a Birthday
    6: Remove a Birthday
    7: See Contacts
    8: Add a Contact
    9: Remove a Contact

    Select a number or type 'Exit' to quit: 

    """)
    # Get Todos
    if user_command == "1":
        print("\nYour to-do list:")
        todos = assistant.get_todos()
        for todo in assistant.get_todos():
            print(f"\n{todo}")
    # Add Todo
    elif user_command == "2":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input.capitalize())
    # Remove Todo
    elif user_command == "3":
        # print todo list to remove
        print("Your todo list:")
        for todo in assistant.get_todos():
            print(f"\n{todo}")
        user_input = input("\nItem to remove from to-do list: ")
        # remove todo
        to_remove = user_input.capitalize()
        if to_remove in assistant.get_todos():
            assistant.remove_todo(to_remove)
        print(f'\n"{user_input}" was removed from list')

    elif user_command == "4":
        print("\nBirthdays:")
        birthdays = assistant.get_birthdays()
        for name, birthday in birthdays.items():
            print(f"{name} birthday is on {birthday}")

    elif user_command == "5":
        name = input("Name of the person to add: ")
        if not assistant.get_birthday(name):
            birthday = input(f"add {name}'s birthday (00/00/0000): ")
            assistant.add_birthday(name, birthday)
            print(f"{name} added to birthday list")

        else:
            print(f"{name} already in birthday list")

    elif user_command == "6":
        name = input("Name of the person to remove: ")
        if assistant.get_birthday(name):
            assistant.remove_birthday(name)
            print(f"removed {name}'s Birthday")

        else:
            print(f"{name}'s birthday doesn't exists")

    elif user_command == "7":
        for name, title in assistant.get_contacts().items():
            print(f"\n{name} -- {title}")

    elif user_command == "8":
        contacts = assistant.get_contacts()
        name = input("\nName of the person to add: ")
        check_name = name.capitalize()
        if not assistant.get_contact(check_name):
            title = input("\nTitle of the person to add: ")
            check_title = title.title()
            assistant.add_contact(name, title)
            print(f'\n"{check_name}" the "{title}" was added')

        else:
            print("contact already exists")

    elif user_command == "9":
        for name, title in assistant.get_contacts().items():
            print(f"\n{name} -- {title}")
        name = input("\n name of person to remove: ")
        if assistant.get_contact(name):
            assistant.remove_contact(name)
            print(f"removed {name} from contact list")

        else:
            print(f"{name} is not a current contact")

    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

# ADD CODE: write data to JSON file
with open("todos.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays, open("contacts.json", "w") as write_contacts:
    json.dump(assistant.get_todos(), write_todos)
    json.dump(assistant.get_birthdays(), write_birthdays)
    json.dump(assistant.get_contacts(), write_contacts)
