from . import app

from flask import (
    render_template, request, redirect
)

from .modules.User import User
from .modules.Category import Category
from .Data import *
from .modules.Note import Note


@app.route('/')
@app.route('/index')
def index():
    update_users()
    update_categories()
    update_notes()

    return render_template('index.html', users=USERS, categories=CATEGORIES, notes=NOTES)


@app.route('/createUser', methods=['POST', 'GET'])
def create_user():
    if request.method == 'POST':
        user_name = request.form["user"]

        user = User(user_name)

        with open('data/UsersList.txt', 'a') as data:
            data.write(f"id: {user.get_id()} name: {user.get_name()}\n")

        return redirect('/')
    else:
        return redirect('/')


@app.route("/<usr>")
def user(usr):
    return f"name: {usr}"


@app.route('/createCategory', methods=['POST', 'GET'])
def create_category():
    if request.method == 'POST':
        category_name = request.form["category"]

        category = Category(category_name)

        with open('data/CategoryList.txt', 'a') as data:
            data.write(f"id: {category.get_id()} name: {category.get_name()}\n")
        return redirect('/')
    else:
        return redirect('/')


@app.route('/createNote', methods=['POST', 'GET'])
def create_note():
    user_id = request.form.get('users')
    category_id = request.form.get('categories')
    cost = request.form["cost"]

    note = Note(user_id, category_id, cost)

    with open('data/NotesList.txt', 'a') as data:
        data.write(
            f"id: {note.get_id()} user_id: {note.get_user_id()} category_id: {note.get_category_id()} date: {note.get_date()} cost: {note.get_cost()}$\n")

    return redirect('/')
