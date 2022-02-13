from flask import Flask

app = Flask(__name__)


# Decorator functions to HTML tag the page contents.
def make_bold(a_function):
    print(a_function.__name__)

    def a_wrapper(*args, **kwargs):
        a_text = a_function()
        return f'<b>{a_text}</b>'

    return a_wrapper


def make_italic(a_function):
    print(a_function.__name__)

    def a_wrapper(*args, **kwargs):
        a_text = a_function()
        return f'<em>{a_text}</em>'

    return a_wrapper


@app.route("/")
@make_bold
@make_italic
def hello_world():
    return "Hello, World!"


@app.route('/bye')
def say_bye():
    return '<h1 style="text-align: center">Bye</h1>' \
           '<img src="https://media.giphy.com/media/v6aOjy0Qo1fIA/giphy.gif" width=400>'


@app.route('/username/<name>')
def greet(name):
    return f'<h1>Hi {name}!</h1>'


@app.route('/username/<name>/<int:age>')
def greet_w_age(name, age):
    return f'Hi {name}, you are {age} years old.'


if __name__ == '__main__':
    app.run(debug=True)
