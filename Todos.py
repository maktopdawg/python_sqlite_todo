import random
from Todo import Todo
from Config import DatabaseOperations

class Todos:
    def __init__(self) -> None:
        self.todos: Todo = []
        self.db = DatabaseOperations()
        
    def create_todo(self,todo) -> None:
        """
            Inserts todo in to database. Inserts todo id, the todo, and completed status

            args:
                Recieves the todo string as an argument

            Returns:
                Return a unique id with five different digits.
        """
        todo_obj = Todo(todo)
        self.db.insert_values(todo_obj.id, todo_obj.todo, todo_obj.complete)
        self.todos.append(todo_obj)

    
    def insert(self, table:str, cols:list(), values:list(), msg:str):
        self.db.insert(table, cols, values, msg)

    
    # def create(self, )


    def select(self,cols:list(), table:str, msg:str):
        self.db.select_values(cols, table, msg)

    
db = DatabaseOperations()
# db.create_table()
todos = Todos()
# uuid = todos.todos.id
todos.select(['ID', 'TODO', 'COMPLETED'], 'TODOs', 'Select Operation Completed Successfully')
# todos.insert('TODOS', ['ID', 'TODO', 'COMPLETED'], [uuid,'Just Chilling', False], 'Record created successfully')