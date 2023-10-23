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

    
    def create(self, name: str, cols:list, msg:str):
        column_definitions = [f"{col[0]} {col[1]} {' '.join(col[2:])}" for col in cols]
        columns = ', '.join(column_definitions)

        self.open_db()
        self.conn.cursor()
        self.conn.execute(f"CREATE TABLE {name.upper()} ({columns})")
        self.conn.commit()
        print(msg)


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