# Give the class a name
class PersonalAssistant:
    def __init__(self, todos, birthdays):
        self.todos = todos
        self.birthdays = birthdays

    # Complete the get_contact function code
    def get_contact(self, name):
        if name:
            return name + " is a " + self.contacts[name]

        else:
            return "no contact with the name " + name

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
        if name in self.birthdays:
            return f"{name}'s birthday is on {self.birthdays}."

        else:
            return "birthday could not be found"

    def add_birthday(self, name, date):
        if name in self.birthdays:
            return f"{name} already exists"

        else:
            new_birthday = self.birthdays[name] = date
            print(f"added {name}'s Birthday")
            return new_birthday

    def remove_birthday(self, name):
        person = name.capitalize()
        if person in self.birthdays:
            self.birthdays.pop(person)
            print(f"removed {person}'s Birthday")
