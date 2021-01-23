from flask import render_template, Blueprint

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
mainbp = Blueprint("main", __name__)


@mainbp.route("/")
def index():
    articles = book["articles"]
    return render_template("index.html", **locals())


@mainbp.route("/<int:pk>")
def detail(pk):
    article = None
    for a in book["articles"]:
        if a["id"] == pk:
            article = a
    return render_template("detail.html", **locals())
