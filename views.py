from . import app

from flask import (
    render_template, request
)

from . import User
from . import Category


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/createUser', methods=['POST', 'GET'])
def create_user():
    user_name = request.form["user"]

    user = User.User(user_name)

    with open('data/UsersList.txt', 'a') as data:
        data.write(f"id: {user.get_id()} name: {user.get_name()}\n")

    return render_template('index.html')


@app.route('/createCategory', methods=['POST', 'GET'])
def create_category():
    category_name = request.form["category"]

    user = Category.Category(category_name)

    with open('data/CategoryList.txt', 'a') as data:
        data.write(f"id: {user.get_id()} name: {user.get_name()}\n")

    return render_template('index.html')

