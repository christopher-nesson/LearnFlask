"""
Master:Chao
Datetime:2021/1/22 9:27
Reversion:1.0
File: demo2.py
flask的路由
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '你好，马猴烧酒'


@app.route('/<int:pk>')
def detail(pk):
    return f"欢迎来到召唤师峡谷"


if __name__ == '__main__':
    app.run(host="192.168.11.29", port="3344", debug=True)
