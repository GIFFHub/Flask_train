from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('top.html')


@app.route('/list')
def item_list():
    return render_template('list.html')


@app.route('/detail/<int:id>')
def item_detail(id):
    return render_template('detail.html', show_id=id)


@app.route("/multiple")
def show_jinja_multiple():
    word1 = "template_engine"
    word2 = "jinja"
    return render_template('jinja/show1.html', temp=word1, jinja=word2)


@app.route("/dict")
def show_jinja_dict():
    words = {
        'temp': "てんぷれーとえんじん",
        'jinja': "神社"
    }
    return render_template('jinja/show2.html', key=words)


@app.route("/list2")
def show_jinja_list():
    hero_list = ['momotaro', 'kintaro', 'urashimataro']
    return render_template('jinja/show3.html', users=hero_list)


class Hero:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        p = 1

    def __str__(self):
        return f'name:{self.name} age:{self.age}'


@app.route("/class")
def show_jinja_class():
    hana = Hero('hanasakajisan', 99)
    return render_template('jinja/show4.html', user=hana)


class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'商品ID:{self.id}商品名：{self.name}'


@app.route("/for_list")
def show_for_list():
    item_list = [Item(1, "dango"), Item(2, "nikuman"), Item(3, "Dorayaki")]
    return render_template("jinja/for_list.html", items=item_list)


@app.route('/if_detail/<int:id>')
def show_if_detail(id):
    item_list = [Item(1, "dango"), Item(2, "nikuman"), Item(3, "Dorayaki")]
    return render_template('if_detail.html', show_id=id, items=item_list)


@app.route('/if/')
@app.route('/if/<target>')
def show_jinja_if(target="colorless"):
    print(target)
    return render_template('jinja/if_else.html', color=target)


@app.route("/filter")
def show_filter_block():
    word = 'pen'
    return render_template('filter/block.html', show_word=word)


if __name__ == '__main__':

    app.run(port=8080)

