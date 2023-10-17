import sqlite3

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
            Creates a table in the databse
        """
        self.open_db()
        self.cursor = self.conn.cursor()
        self.conn.execute('CREATE TABLE TODOS (ID TEXT PRIMARY KEY NOT NULL, TODO TEXT NOT NULL, COMPLETED BOOLEAN NOT NULL)')
        self.conn.commit()
        print('Table created successfully')

    def insert_values(self, id: str, todo: str, completed: bool):
        """
            Inserts values passed in as arguments into the database

            args:
                Recieves the todo id, todo string, and todo completion status
        """
        self.cursor.execute('INSERT INTO TODOS (ID, TODO, COMPLETED) VALUES (?, ?, ?)', (id, todo, completed))
        self.conn.commit()
        print("Record created successfully")