import datetime
import os
import sqlite3
from bottle import route, request, abort, run, response, static_file, template, TEMPLATE_PATH

import config
import model

TEMPLATE_PATH.append("./template")

@route("/")
def welcome_service():
        print("config.DATA_PERSISTENCE_FLAG=" + str(config.DATA_PERSISTENCE_FLAG))
        print("config.DATABASE_LOCATION" + str(config.DATABASE_LOCATION))

        print("-- database setup start --")
        ret = model.init_db()
        if ret is True:
                print("-- database setup success --")
        else:
                print("-- database setup failed --")

        response.headers['Access-Control-Allow-Origin'] = '*'
        return "Welcome to the MyIdea-IO!!"


@route("/top")
def top_page():
        test = "hogehoge"
        return template("top.html", test=test)


@route("/files/<file_path:path>")
def ret_files(file_path):
        return static_file(file_path, root="./static")


if __name__ == "__main__":
        run(host=config.SERVER_HOST_ADDR, port=int(os.environ.get("PORT", config.SERVER_HOST_PORT)))
