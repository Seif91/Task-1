import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('Bewerbung')
        self.create_todo_table()

    def create_todo_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS "Bewerbung" (
                id INTEGER PRIMARY KEY,
                Title TEXT,
                Description TEXT            
            );
        """

        self.conn.execute(query)


