import os

from flask import Flask

from views.main import mainbp
from views.user import userbp

app = Flask(__name__)
app.register_blueprint(mainbp)
app.register_blueprint(userbp)

app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run(debug=True)
