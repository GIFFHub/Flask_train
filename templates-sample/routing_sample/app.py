from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Topページ</h1>"


@app.route("/list")
def item_list():
    return "商品一覧ページ"


@app.route("/detail")
def item_detail():
    return "商品詳細ページ"


if __name__ == '__main__':
    app.run(port=8080)


