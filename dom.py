from flask import Flask, render_template, url_for, request, session, redirect, jsonify, url_for
from bson.json_util import dumps, ObjectId
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.secret_key = 'secret_key'

app.config['MONGO_URI'] = "mongodb://nusta_coder:shadow7431@cluster0-shard-00-00-kwsyr.mongodb.net:27017,cluster0-shard-00-01-kwsyr.mongodb.net:27017,cluster0-shard-00-02-kwsyr.mongodb.net:27017/game?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route('/')
def index():
    user = mongo.db.login.find()
    cnt = 0
    for i in user:
        cnt += 1
    resp = str(cnt)
    return render_template("index.html", cnt=resp)


@app.route('/levelone', methods=['POST'])
def level_one():
    a = request.form['username']
    b = request.form['email']

    if a and b and request.method == 'POST':
        id = mongo.db.login.insert({"name": a, "email": b})
    return render_template("one.html", a=a, b=b)


@app.route('/feedback/<id>', methods=['POST'])
def send_feedback(id):

    a = request.form['username']
    b = request.form['email']
    c = request.form['feedback']
    d = request.form['level']
    if a and b and c and request.method == 'POST':
        n = mongo.db.box.insert(
            {"name": a, "email": b, "level": d, "feedback": c})
    if id == "index":
        return redirect(url_for('index'))
    elif id == "one":
        return redirect(url_for('level_one'))
    elif id == "two":
        return redirect(url_for('toLevelTwo'))
    elif id == "three":
        return redirect(url_for('toLevelThree'))
    elif id == "four":
        return redirect(url_for('toLevelFour'))
    elif id == "five":
        return redirect(url_for('toLevelFive'))
    elif id == "six":
        return redirect(url_for('toLevelSix'))
    elif id == "seven":
        return redirect(url_for('toLevelSeven'))
    elif id == "eight":
        return redirect(url_for('toLevelEight'))
    elif id == "nine":
        return redirect(url_for('toLevelTen'))
    elif id == "ten":
        return redirect(url_for('endGame'))


@app.route('/levelone/shadow')
def toLevelError():
    resp = jsonify(
        "this is not how you type url...correct url is '/shadow' not '/levelone/shadow'")
    return resp


@app.route('/shadow')
def toLevelTwo():
    return render_template("two.html")


@app.route('/20190201')
def toLevelThree():
    return render_template("three.html")


@app.route('/11')
def toLevelFour():
    return render_template("four.html")


@app.route('/z')
def toLevelFive():
    return render_template("five.html")


@app.route('/499')
def toLevelSix():
    return render_template("six.html")


@app.route('/bookkeeper')
def toLevelSeven():
    return render_template("seven.html")


@app.route('/thirteen')
def toLevelEight():
    return render_template("eight.html")


@app.route('/sixty')
def toLevelTen():
    return render_template("ten.html")


@app.route('/60')
def toLevel10():
    return render_template("ten.html")


@app.route('/0xcd0aaedfd83a4dabb330a92a60f3ca67b1db1d28')
def endGame():
    return render_template("end.html")


if __name__ == '__main__':
    app.run(debug=True)
