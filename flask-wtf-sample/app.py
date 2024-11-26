from flask import Flask, render_template, session, redirect, url_for
import os
from forms import InputForm
app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('output'))
    if 'name' in session:
        form.name.data = session['name']
    if 'email' in session:
        form.email.data = session['email']
    return render_template('input.html', form=form)


@app.route('/output')
def output():
    return render_template('output.html')


if __name__ == '__main__':
    app.run(port=8080)



