from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

book = {
    "name": "斗破苍穹",
    "auhtor": "于智文",
    "articles": [
        {
            "id": 101,
            "title": "第一章 陨落的天才",
            "content": "　　望着测验魔石碑上面闪亮得甚至有些刺眼的五个大字，少年面无表情，唇角有着一抹自嘲，紧握的手掌，因为大力，而导致略微尖锐的指甲深深的刺进了掌心之中，带来一阵阵钻心的疼痛…"
        },
        {
            "id": 102,
            "title": "第二章 斗气大陆",
            "content": "　　山崖之颠，萧炎斜躺在草地之上，嘴中叼中一根青草，微微嚼动，任由那淡淡的苦涩在嘴中弥漫开来…"
        },
        {
            "id": 103,
            "title": "第三章 客人",
            "content": "　　床榻之上，少年闭目盘腿而坐，双手在身前摆出奇异的手印，胸膛轻微起伏，一呼一吸间，形成完美的循环，而在气息循环间，有着淡淡的白色气流顺着口鼻，钻入了体内，温养着骨骼与肉体。"
        }

    ]
}
users = [
    {
        "email": "496575233@qq.com",
        "password": "123456"
    }
]
currentuser = None


@app.route("/")
def index():
    global currentuser
    user = currentuser
    print(user, "-------")
    articles = book["articles"]
    return render_template("index.html", **locals())


@app.route("/<int:pk>")
def detail(pk):
    global currentuser
    user = currentuser
    article = None
    for a in book["articles"]:
        if a["id"] == pk:
            article = a
    return render_template("detail.html", **locals())


@app.route("/login", methods=["GET", "POST"])
def login():
    global currentuser
    if request.method == "GET":
        return render_template("login.html", **locals())
    elif request.method == "POST":
        user = None
        email = request.form.get("email")
        password = request.form.get("password")
        for u in users:
            if u["email"] == email and u["password"] == password:
                currentuser = u
                print(currentuser, "====")
                return redirect(url_for("index"))
        print("登录失败")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    global currentuser
    currentuser = None
    user = currentuser
    return redirect(url_for("index"))


@app.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        return render_template("regist.html", **locals())
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        global users
        users.append({
            "email": email,
            "password": password
        })
        print("当前用户有", users)
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)