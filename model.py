import datetime
import sqlite3
import config
import sys


def init_db():
    ret = True

    now = datetime.datetime.now()
    connection = sqlite3.connect(config.DATABASE_LOCATION)
    try:
        coursor = connection.cursor()
        connection.execute(
            "CREATE TABLE IF NOT EXISTS userInfo (userId TEXT PRIMARY KEY NOT NULL, createDate TEXT)")
        connection.execute(
            "CREATE TABLE IF NOT EXISTS inputData (userKey TEXT NOT NULL, inText TEXT NOT NULL, createDate TEXT, PRIMARY KEY(userKey, inText))")
        connection.execute(
            "CREATE TABLE IF NOT EXISTS outputData (userKey TEXT NOT NULL, outText TEXT NOT NULL, createDate TEXT, PRIMARY KEY(userKey, outText))")

    except sqlite3.Error as e:
        ret = False
        print("sqlite3 error occurred:", e.args[0])

    connection.commit()
    connection.close()

    return ret


def getUserInfo(userId: str):
    print("getUserInfo in.")

    # DataBase init.
    init_db()

    result = None
    connection = sqlite3.connect(config.DATABASE_LOCATION)
    # try:
    coursor = connection.cursor()
    result = coursor.execute(
        "SELECT userId, createDate FROM userInfo WHERE userId ='" + userId + "'").fetchall()
    if len(result) is 0:
        result = None
    # except:
    #    result = None
    #    print("Error occurred:", sys.exc_info()[0])'

    connection.close()

    print(result)
    print("getUserInfo out.")
    return result


def registUser(userId: str, createDate: str):
    print("registUser in.")
    ret = True

    # DataBase init.
    init_db()

    infoTmp = getUserInfo(userId)
    print(infoTmp)
    if infoTmp is None:
        connection = sqlite3.connect(config.DATABASE_LOCATION)
        try:
            coursor = connection.cursor()
            insert_sql = "INSERT INTO userInfo (userId, createDate) VALUES (?, ?)"
            insert_prm = (userId, createDate)
            coursor.execute(insert_sql, insert_prm)
            connection.commit()
            ret = True
        except:
            ret = False
            print("Error occurred:", sys.exc_info()[0])
        connection.close()
    else:
        ret = False

    print(ret)
    print("registUser out. ")
    return ret


def getInputData(userId: str):
    print("getInputData in.")

    # DataBase init.
    init_db()

    result = None
    connection = sqlite3.connect(config.DATABASE_LOCATION)
    try:
        coursor = connection.cursor()
        result = coursor.execute(
            "SELECT inText, createDate FROM inputData WHERE userKey ='" + userId + "'").fetchall()
    except:
        result = None
        print("Error occurred:", sys.exc_info()[0])

    connection.close()

    print("getInputData out.")
    return result


def getOutputData(userId: str):
    print("getOutputData in.")

    # DataBase init.
    init_db()

    result = None
    connection = sqlite3.connect(config.DATABASE_LOCATION)
    try:
        coursor = connection.cursor()
        result = coursor.execute(
            "SELECT outText, createDate FROM outputData WHERE userKey ='" + userId + "'").fetchall()
    except:
        result = None
        print("Error occurred:", sys.exc_info()[0])

    connection.close()

    print("getOutputData out.")
    return result


def registInputData(userId: str, inText: str ,createDate: str):
    print("registInputData in.")
    ret = True

    # DataBase init.
    init_db()

    infoTmp = getUserInfo(userId)
    print(infoTmp)
    if infoTmp is None:
        ret = False
    else:
        connection = sqlite3.connect(config.DATABASE_LOCATION)
        try:
            coursor = connection.cursor()
            insert_sql = "INSERT INTO inputData (userKey, inText, createDate) VALUES (?, ?, ?)"

            insert_prm = (userId, inText, createDate)
            coursor.execute(insert_sql, insert_prm)
            connection.commit()
            ret = True
        except:
            ret = False
            print("Error occurred:", sys.exc_info()[0])
        connection.close()

    print(ret)
    print("registInputData out. ")
    return ret


def registOutputData(userId: str, inText: str ,createDate: str):
    print("registOutputData in.")
    ret = True

    # DataBase init.
    init_db()

    infoTmp = getUserInfo(userId)
    print(infoTmp)
    if infoTmp is None:
        ret = False
    else:
        connection = sqlite3.connect(config.DATABASE_LOCATION)
        try:
            coursor = connection.cursor()
            insert_sql = "INSERT INTO outputData (userKey, outText, createDate) VALUES (?, ?, ?)"

            insert_prm = (userId, inText, createDate)
            coursor.execute(insert_sql, insert_prm)
            connection.commit()
            ret = True
        except:
            ret = False
            print("Error occurred:", sys.exc_info()[0])
        connection.close()

    print(ret)
    print("registOutputData out. ")
    return ret
