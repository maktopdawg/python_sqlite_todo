import random
from Todo import Todo
from Config import DatabaseOperations

class Todos:
    def __init__(self) -> None:
        self.todos: Todo = []
        self.db = DatabaseOperations()
        
    def create_todo(self,todo) -> None:
        todo_obj = Todo(todo)
        self.db.insert_values(todo_obj.id, todo_obj.todo, todo_obj.complete)
        self.todos.append(todo_obj)

    
db = DatabaseOperations()
# db.create_table()
todos = Todos()
todos.create_todo('Learn OOP')
# for i in range(5):
#     todos.create_todo(random.choice(['hey', 'love', 'the', 'Key', 'primary']))
# print(todos.todos)
# todos.todos[0][2] = True
# print(todos.todos)