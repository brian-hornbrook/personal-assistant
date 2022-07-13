# Give the class a name
class PersonalAssistant:
    def __init__(self, todos):
        self.todos = todos

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

    def get_birthday(self, name):
        if name == "Tomas Edison":
            return "Thomas's birthday is: 02/11/1847"

        elif name == "Henry Ford":
            return "Henry's birthday is: 07/30/1863"

        elif name == "Ada Lovelace":
            return "Ada's birthday is: 12/10/1815"

        return "can't find a birthday!" + name
