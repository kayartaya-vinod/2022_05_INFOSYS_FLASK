import sqlite3

if __name__ == '__main__':
    with sqlite3.connect('mydb.sqlite3') as conn:
        print('Got a connection')
        with open('db_script.sql', encoding="utf8") as file:
            conn.executescript(file.read())
            print('Commands in db_script.sql were executed successfully.')
