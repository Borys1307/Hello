from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
names = set()


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', names=names)


@app.route('/add_name', methods=['POST'])
def add_name():
    name = request.form['Insert your name']
    if name not in names:
        names.add(name)
        to_flash = 'Привіт, ' + name
    else:
        to_flash = 'Вже бачились, ' + name
    flash(to_flash)
    return redirect(url_for('hello'))
