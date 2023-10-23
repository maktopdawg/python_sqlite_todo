import random
from Todo import Todo
from Config import DatabaseOperations

class Todos:
    def __init__(self) -> None:
        self.todos: Todo = []
        self.db = DatabaseOperations()

    
    def insert(self, table:str, cols:list(), values:list(), msg:str):
        todo_obj = Todo(values[0])
        values.insert(0,todo_obj.id)
        values.append(todo_obj.complete)
        self.db.insert(table, cols, values, msg)


    def select(self,cols:list(), table:str, msg:str):
        self.db.select_values(cols, table, msg)

    def run_program(self):
        action = input('What do you want to do? ').lower()
        match action:
            case 'create_table':
                self.db.create('TODOS', [['ID', 'TEXT', 'PRIMARY KEY', 'NOT NULL'], ['TODO', 'TEXT', 'NOT NULL'], ['STATUS', 'BOOLEAN', 'NOT NULL']], 'Table created successfully')
            case 'new_todo':
                todo = input('Enter Task: ')
                self.insert('TODOS', ['ID', 'TODO', 'STATUS'], [todo], 'Record created successfully')
            case 'show_all':
                self.select(['ID', 'TODO', 'STATUS'], 'TODOS', 'All records fetched successfully')