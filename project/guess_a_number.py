from flask import Flask
import random as rdn

global nr_to_guess
app = Flask(__name__)


@app.route('/')
def home():
    return '<h2>Guess a number between 0 and 9</h2>' \
           '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'


@app.route("/<int:user_guess>")
def guess(user_guess):
    global nr_to_guess
    if user_guess == nr_to_guess:
        out_html = f'<h1>Congratulations, you guessed it right: {nr_to_guess}</h1>'
        nr_to_guess = rdn.randint(0, 9)
        print(nr_to_guess)
    else:
        out_html = f'<h1 style="color: red">Wrong, Guess again!</h1>'
    return out_html


if __name__ == '__main__':
    nr_to_guess = rdn.randint(0, 9)
    print(nr_to_guess)
    app.run(debug=True)