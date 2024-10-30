#!/usr/bin/env python

# Author: Polina Salnikova
# Notes:
#  - Метод OPTIONS включен на всех роутах, т.к. в Flask его отключить нельзя

from flask import Flask, Response, request, abort, render_template
import hashlib

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<p>Привет! Это сайт с нескушным дизайном!</p><p><a href="/get">get</a> <a href="/post">post</a> <a href="/head">head</a> <a href="/options">options</a></p>'

@app.route("/get", methods=['GET'])
def get_func():
    if request.method == 'GET':                 # Flask очень явно не хочет выпонять требования, 
                                                # которые ты перед ним ставишь, 
                                                # поэтому проверку на метод запроса считаю обязательной
        if request.args.get("username"):
            return render_template('login.html', user='value=' + request.args.get("username"))
        return render_template('login.html', user="")
    else:
        abort(405)                              # Метод не поддерживается

@app.route("/post", methods=['POST'])
def post_func():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password: 
            return render_template("yota.html")
        else: 
            return render_template("lose.html")
    else:
        abort(405)

@app.route("/head", methods=['HEAD'])
def head_func():
    if request.method == 'HEAD':
        response = Response()
        response.headers["Attension"] = "@Slim_Shady, please stand up!"
        return response
    else:
        abort(405)

@app.route("/options", methods=['OPTIONS'])
def options_func():
    if request.method == 'OPTIONS':
        return "<p>Hello, World!</p>"
    else:
        abort(405)
