import sqlite3


class Model:
    def __init__(self):
        print("Model !")
        self._con = sqlite3.connect('example.db')


class CreateDB:
    def __init__(self, filename):
        self._con = sqlite3.connect(filename)
        self._cur = self._con.cursor()

    def updateDB(self, query):
        try:
            for row in self._cur.execute(query):
                print(row)
            self._con.commit()
        except sqlite3.OperationalError as err:
            print(err)
