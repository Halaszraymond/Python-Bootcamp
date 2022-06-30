from flask import Flask

app = Flask(__name__)


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is your first blogpost, {user.name}!")


new_user = User("Raymond")
new_user.is_logged_in = True
create_blog_post(new_user)
