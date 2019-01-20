﻿import datetime
import os
import sqlite3
from bottle import route, request, abort, run, response, redirect, static_file, template, TEMPLATE_PATH

import config
import model
import sys

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
        return template("top.html", test="to the start page...")


@route("/start")
def top_page():
        test = "hogehoge"
        return template("start.html", test=test)


@route("/user_create", method=['POST'])
def user_create():
        print("NAK::user create in")
        userName = request.forms.get("userId")
        print(userName)
        now = datetime.datetime.now()
        print(now)
        retVal = model.registUser(userName, now)
        if retVal is False:
                redirect("/start?user=faild")
        else:
                redirect("/start?user=success")


@route("/files/<file_path:path>")
def ret_files(file_path):
        return static_file(file_path, root="./static")


if __name__ == "__main__":
        run(host=config.SERVER_HOST_ADDR, port=int(os.environ.get("PORT", config.SERVER_HOST_PORT)))
