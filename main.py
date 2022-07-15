# imports PersonalAssistant.py file
from PersonalAssistant import PersonalAssistant
import json

# ADD CODE: open JSON file and pass data to PersonalAssistant class
with open("todos.json", "r") as todos, open("birthdays.json", "r") as birthdays:
    todo_list = json.load(todos)
    birthday_list = json.load(birthdays)
    assistant = PersonalAssistant(todo_list, birthday_list)

done = False

while not done:
    user_command = input("""
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list
    4: Get Birthdays
    5: Add a Birthday
    6: Remove a Birthday

    Select a number or type 'Exit' to quit: 

    """)
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input.capitalize())
    # Remove Todo
    elif user_command == "2":
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
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list:")
        todos = assistant.get_todos()
        for todo in assistant.get_todos():
            print(f"\n{todo}")

    elif user_command == "4":
        print("\nBirthdays:")
        birthdays = assistant.get_birthdays()
        for name, birthday in birthdays.items():
            print(f"{name} birthday is on {birthday}")

    elif user_command == "5":
        name = input("Name of the person to add: ")
        birthday = input(f"add {name}'s birthday (00/00/0000): ")
        assistant.add_birthday(name.capitalize(), birthday)

    elif user_command == "6":
        name = input("Name of the person to remove: ")
        assistant.remove_birthday(name)

    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

# ADD CODE: write data to JSON file
with open("todos.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays:
    json.dump(assistant.get_todos(), write_todos)
    json.dump(assistant.get_birthdays(), write_birthdays)
