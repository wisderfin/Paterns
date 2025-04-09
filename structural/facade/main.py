import sqlite3

class SimpleSQLite:
    def __init__(self, path: str):
        self.path = path
        self.connection: sqlite3.Connection = None

    def _connect(self) -> sqlite3.Connection:
        if self.connection is None:
            self.connection = sqlite3.connect(self.path)
        return self.connection

    def close(self) -> None:
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def create_table(self, table: str, columns: dict[str, str]) -> None:
        cursor = self._connect().cursor()
        column_definitions = ', '.join([f"{c} {t}" for c, t in columns.items()])
        query = f'CREATE TABLE IF NOT EXISTS {table} ({column_definitions})'
        cursor.execute(query)
        self._connect().commit()

    def insert(self, table: str, data: dict[str, any]) -> None:
        cursor = self._connect().cursor()
        columns = ', '.join([key for key in data.keys()])
        placeholders = ', '.join(['?' for _ in data])
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        cursor.execute(query, tuple(data.values()))
        self._connect().commit()

    def select_all(self, table: str) -> list:
        cursor = self._connect().cursor()
        query = f'SELECT * FROM {table}'
        cursor.execute(query)
        return cursor.fetchall()


if __name__ == '__main__':
    db = SimpleSQLite('structural/facade/new.db')
    db.create_table('names', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'age': 'INTEGER'})
    db.insert('names', {'name': 'wisderfin', 'age': 20})

    print(db.select_all('names'))

    db.close()

    
