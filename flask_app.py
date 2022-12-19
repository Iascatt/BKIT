'''
Для запуска сервиса используем команду командной строки:
flask --app num run
'''
from flask import Flask
from sequence import catalan

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Returning the Catalan numbers!</p>"


@app.route('/num/<int:cnt>')
def get_fib(cnt):
    res = [catalan(i) for i in range(cnt)]
    return res
