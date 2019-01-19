import datetime
import sqlite3
import config

def init_db():
    ret = True

    now = datetime.datetime.now()
    connection = sqlite3.connect(config.DATABASE_LOCATION)
    try:
        coursor = connection.cursor()
        connection.execute("CREATE TABLE IF NOT EXISTS variable (userId TEXT PRIMARY KEY NOT NULL, createDate TEXT)")
        connection.execute("CREATE TABLE IF NOT EXISTS stack (userKey TEXT NOT NULL, ioText TEXT NOT NULL, createDate TEXT, PRIMARY KEY(userKey, ioText))")            

    except sqlite3.Error as e:
        ret = False
        print("sqlite3 error occurred:", e.args[0])

    connection.commit()
    connection.close()

    return ret

