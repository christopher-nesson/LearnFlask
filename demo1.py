# 1引入flask模块
from flask import Flask
# 2构建Flask应用
app = Flask(__name__)
# 3启动应用
if __name__ == '__main__':
    app.run()
