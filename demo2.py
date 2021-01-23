"""
flask的路由
"""

from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "欢迎来到Flask首页"


@app.route("/<int:pk>")
def detail(pk):
    return f"欢迎来到Flask页面{pk}"


if __name__ == '__main__':
    # debug=True 可以启动热更新 代码发生变化 不用重启服务器
    app.run(host="192.168.11.22", port="6789", debug=True)
