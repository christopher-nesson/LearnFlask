"""
Master:Chao
Datetime:2021/1/22 10:12
Reversion:1.0
File: demo3.py
Flask的模板文件
"""
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
