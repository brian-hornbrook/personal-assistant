# Give the class a name
class PersonalAssistant:
    def __init__(self, todos, birthdays, contacts):
        self.todos = todos
        self.birthdays = birthdays
        self.contacts = contacts

    # Complete the get_contact function code
    def add_todo(self, new_item):
        self.todos.append(new_item)

    def remove_todo(self, todo_item):
        if todo_item in self.todos:
            self.todos.remove(todo_item)

    def get_todos(self):
        return self.todos

    def get_birthdays(self):
        return self.birthdays

    def get_birthday(self, name):
        check_name = name.capitalize()
        if check_name in self.birthdays:
            return self.birthdays

    def add_birthday(self, name, date):
        check_name = name.capitalize()
        if check_name in self.birthdays:
            return None

        else:
            self.birthdays[check_name] = date

    def remove_birthday(self, name):
        person = name.capitalize()
        if person in self.birthdays:
            self.birthdays.pop(person)

    def get_contacts(self):
        return self.contacts

    def get_contact(self, name):
        check_name = name.capitalize()
        if check_name in self.contacts:
            return self.contacts

    def add_contact(self, name, title):
        check_name = name.capitalize()
        check_title = title.title()
        self.contacts[check_name] = check_title

    def remove_contact(self, name):
        check_name = name.capitalize()
        if check_name in self.contacts:
            self.contacts.pop(check_name)
