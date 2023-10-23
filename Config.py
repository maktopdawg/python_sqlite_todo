import sqlite3
import Todo

class DatabaseOperations:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('test.db')
        self.cursor = self.conn.cursor()


    def open_db(self):
        """
            Connects to the exisiting database and creates one if it doesn't exist
        """
        try:
            self.conn = sqlite3.connect('test.db')
            print('Database opened successfully')
        except Exception as e:
            print(e)


    def create_table(self):
        """
            Creates a table in the database
        """
        self.open_db()
        self.conn.cursor()
        self.conn.execute('CREATE TABLE TODOS (ID TEXT PRIMARY KEY NOT NULL, TODO TEXT NOT NULL, COMPLETED BOOLEAN NOT NULL)')
        self.conn.commit()
        print('Table created successfully')

    
    def create(self, name:str, cols:list(list()), types:list()):
        q = f"CREATE TABLE {name.upper()} ({', '.join({j for j in i} for i in cols)})"


    # def insert_values(self, id: str, todo: str, completed: bool):
    #     """
    #         Inserts values passed in as arguments into the database

    #         args:
    #             Recieves the todo id, todo string, and todo completion status
    #     """
    #     self.cursor.execute('INSERT INTO TODOS (ID, TODO, COMPLETED) VALUES (?, ?, ?)', (id, todo, completed))
    #     self.conn.commit()
    #     print("Record created successfully")


    def insert(self, table:str, cols:list(), values:list(), msg:str):
        try:
            self.cursor.execute(f"INSERT INTO {table.upper()} ({', '.join(i for i in cols)}) VALUES (?, ?, ?)", tuple(values))
            self.conn.commit()
            print(msg)
        except Exception as e:
            print('Operation failed')
            print(e)


    def select_values(self, cols:list(), table:str, msg:str):
        for item in self.conn.execute(f"SELECT {', '.join(i for i in cols)} from {table.upper()}"):
            print(f"ID = {item[0]}\nTODO = {item[1]}\nCOMPLETED = {item[2]}\n")
        print(msg)