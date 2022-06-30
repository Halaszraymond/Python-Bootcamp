from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def bold_wrapper():
        return "<b>" + function() + "</b>"
    return bold_wrapper


def make_italic(function):
    def emphasis_wrapper():
        return "<em>" + function() + "</em>"
    return emphasis_wrapper


def make_underline(function):
    def underline_wrapper():
        return "<u>" + function() + "</u>"
    return underline_wrapper


@app.route('/')
@make_bold
@make_italic
@make_underline
def say_hello():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)