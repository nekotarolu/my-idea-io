import datetime
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
    nowStr = now.strftime('%Y%m%d%H%M%S')
    print(nowStr)
    retVal = model.registUser(userName, nowStr)
    if retVal is False:
        redirect("/start?user=faild")
    else:
        redirect("/user?userId=" + userName)


@route("/user_login", method=['POST'])
def user_create():
    print("NAK::user create in")
    userName = request.forms.get("userId")
    print(userName)
    retVal = model.getUserInfo(userName)
    if retVal is None:
        redirect("/start?user=faild")
    else:
        redirect("/user?userId=" + userName)


@route("/user")
def user_page():
    userId = request.query.userId
    print(userId)
    userInfo = model.getUserInfo(userId)
    if userInfo is None:
        print("userId is None...")
        redirect("/start?user=faild")
    else:
        inList = model.getInputData(userId)
        inputList = []
        for inData in inList:
            inputList.append({
                "inText": inData[0],
                "createDate": inData[1]
            })

        outList = model.getOutputData(userId)
        outputList = []
        for outData in outList:
            outputList.append({
                "outText": outData[0],
                "createDate": outData[1]
            })

        return template("userpage.html", userId=userInfo[0][0], inputList=inputList, outputList=outputList)


@route("/input_regist", method=['POST'])
def input_regist():
    userId = request.query.userId
    print(userId)
    inputText = request.forms.get("inputText")
    print(inputText)
    now = datetime.datetime.now()
    nowStr = now.strftime('%Y/%m/%d %H:%M.%S')
    model.registInputData(userId, str(inputText), nowStr)
    redirect("/user?userId=" + userId)


@route("/output_regist", method=['POST'])
def output_regist():
    userId = request.query.userId
    print(userId)
    outputText = request.forms.get("outputText")
    print(outputText)
    now = datetime.datetime.now()
    nowStr = now.strftime('%Y/%m/%d %H:%M.%S')
    model.registOutputData(userId, str(outputText), nowStr)
    redirect("/user?userId=" + userId)


@route("/input_delete/<target_text>")
def input_delete(target_text):
    userId = request.query.userId
    print(userId)
    print(target_text)
    redirect("/user?userId=" + userId)


@route("/output_delete/<target_text>")
def output_delete(target_text):
    userId = request.query.userId
    print(userId)
    print(target_text)
    redirect("/user?userId=" + userId)

@route("/files/<file_path:path>")
def ret_files(file_path):
    return static_file(file_path, root="./static")


if __name__ == "__main__":
    run(host=config.SERVER_HOST_ADDR, port=int(
        os.environ.get("PORT", config.SERVER_HOST_PORT)))
