from os import read, write
from flask import Flask, request, redirect, render_template, jsonify, url_for
import csv, json, logging

import pandas as pd
import uuid
import os.path


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("spa.html")


@app.route("/login", methods=['POST',"GET"])
def login():
    if request.method == "POST":
        name = request.get_json('uname')
        password = request.get_json('pword')
        return "Logged In"
            
        
@app.route("/display", methods=['GET'])
def display():
    if request.method == "GET":
        det = []
        with open("newfile5.csv", "r") as rFile:
            reader = csv.DictReader(rFile)
            for row in reader:
                detial = dict(row)
                det.append(detial)         
                # print(det) 
            return jsonify(det)


@app.route("/inputs", methods=["POST", "GET"])
def input():
    if request.method == 'POST':
        params = request.get_json(force=True)
        name_r= params.get('name')
        comments_r = params.get('comment')
        uid = uuid.uuid4() 
        filename = "newfile5.csv"
        with open(filename,"a") as file:
            file_is_empty = os.stat(filename).st_size == 0
            writer = csv.writer(file, lineterminator='\n')
            fields = ["UID", "Name", "Comment"]
            if file_is_empty:
                writer.writerow(fields)
            writer.writerow([uid, name_r, comments_r])
        return jsonify({"UID":uid, "name":name_r, "comment":comments_r})
       



if __name__ == "__main__":
    app.run(debug=True)