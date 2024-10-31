#!/usr/bin/env python
# Author: Polina Salnikova

from flask import Flask, Response, request, abort, render_template
import hashlib

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<p>Привет! Это сайт с нескушным дизайном!</p><p><a href="/get">get</a> <a href="/post">post</a> <a href="/head">head</a> <a href="/options">options</a></p>'

@app.route("/get", methods=['GET', 'HEAD', 'OPTIONS'])
def get_func():
    if request.method == 'GET':                 # Flask очень явно не хочет выпонять требования, 
                                                # которые ты перед ним ставишь, 
                                                # поэтому проверку на метод запроса считаю обязательной
        if request.args.get("username"):
            response = Response(render_template('login.html', user='value=' + request.args.get("username")))
            response.headers["username"] = request.args.get("username")
            return response
        return render_template('login.html', user="")
    else:
        abort(405)                              # Метод не поддерживается

@app.route("/post", methods=['POST', 'OPTIONS'])
def post_func():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password: 
            response = Response(render_template("yota.html"))
        else: 
            response = Response(render_template("lose.html"))
        response.headers["username"] = username
        response.headers["password"] = password
        return response
    else:
        abort(405)

@app.route("/head", methods=['HEAD', 'OPTIONS'])
def head_func():
    if request.method == 'HEAD':
        response = Response()
        response.headers["Attention"] = "@Slim_Shady, please stand up!"
        return response
    else:
        abort(405)

@app.route("/options", methods=['OPTIONS'])
def options_func():
    if request.method == 'OPTIONS':
        response = Response("<p>Hello, World!</p>")
        response.headers["Allow"] = "OPTIONS"
        return response
    else:
        abort(405)
